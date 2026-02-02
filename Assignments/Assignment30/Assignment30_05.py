import sys
import os

def FindOccurance(FName, string):
    Flag = False

    Ret = os.path.exists(FName)
    if Ret == False:
        print("Folder not exists")
        return
    
    fobj = open(FName,"r")

    for line in fobj:
        # tokens = line.split()
        if string in line:
            Flag = True
            break
        
    fobj.close()
    return Flag

def main():

    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        print("Usage: Assignment29_03.py File1.txt StringToFind")
        return()
    
    Ret = FindOccurance(sys.argv[1], sys.argv[2])

    if(Ret == True):
        print("Word is present")
    else:
        print("Word is absent")


if __name__ == "__main__":
    main()