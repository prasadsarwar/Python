import sys
import os

def CompareFiles(FName1, FName2):
    Flag = True

    Ret = os.path.exists(FName1)
    if(Ret == False):
        print(f"{FName1} does not exists")
        return
    
    Ret = os.path.exists(FName2)
    if(Ret == False):
        print(f"{FName2} does not exists")
        return
    
    fobj1 = open(FName1, "r")
    fobj2 = open(FName2, "r")

    Buffer1 = fobj1.read(1024)
    Buffer2 = fobj2.read(1024)

    while((len(Buffer1) > 0) or (len(Buffer2) > 0)):
        
        if(Buffer1 != Buffer2):
            Flag = False
            break

        Buffer1 = fobj1.read(1024)
        Buffer2 = fobj2.read(1024)

    fobj1.close()
    fobj2.close()

    return Flag


def main():

    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        print("Usage: Assignment29_03.py File1.txt File2.txt")
        return()
    
    Ret = CompareFiles(sys.argv[1], sys.argv[2])

    if(Ret == True):
        print("Success")
    else:
        print("Failure")

if __name__ == "__main__":
    main()