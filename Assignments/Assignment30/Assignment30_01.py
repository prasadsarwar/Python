import sys
import os

# def CountLines(FName):
#     iCount = 0

#     Ret = os.path.exists(FName)
#     if(Ret == False):
#         print(f"{FName} does not exists")
#         return
    
#     fobj = open(FName,"r")

#     Buffer = fobj.readlines()

#     print(len(Buffer))
    
#     iCount = len(Buffer)

#     fobj.close()

#     return iCount


def CountLines(FName):
    iCount = 0

    Ret = os.path.exists(FName)
    if(Ret == False):
        print(f"{FName} does not exists")
        return
    
    fobj = open(FName,"r")

    for line in fobj:
        iCount  = iCount + 1

    fobj.close()

    return iCount

def main():

    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Usage: Assignment29_03.py File1.txt")
        return()
    
    Ret = CountLines(sys.argv[1])

    print("Number of lines:",Ret)


if __name__ == "__main__":
    main()