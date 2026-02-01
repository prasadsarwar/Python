import sys
import os

def CopyFile(ExistingFile, NewFile):
    Ret = os.path.exists(ExistingFile)
    if(Ret == False):
        print(f"{ExistingFile} does not exists")
        return
    
    fobj1 = open(ExistingFile, "r")
    fobj2 = open(NewFile, "w")

    Buffer = fobj1.read(1024)

    while(len(Buffer) > 0):
        fobj2.write(Buffer)
        Buffer = fobj1.read(1024)

    fobj1.close()
    fobj2.close()


def main():

    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        print("Usage: Assignment29_03.py ExistingFileName.txt NewFileName.txt")
        return()
    
    CopyFile(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()