import sys
import os

def CountWords(FName):
    iCount = 0

    Ret = os.path.exists(FName)
    if(Ret == False):
        print(f"{FName} does not exists")
        return
    
    fobj = open(FName,"r")

    for line in fobj:
        tokens = line.split()
        iCount = iCount + len(tokens)

    fobj.close()

    return iCount

def main():

    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Usage: Assignment29_03.py File1.txt")
        return()
    
    Ret = CountWords(sys.argv[1])

    print("Number of words:",Ret)


if __name__ == "__main__":
    main()