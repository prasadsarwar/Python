import sys
import os

def FileSearch(DirName, ExtName):
    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("Path does not exists")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    if(ExtName[0] != "."):
        print("Invalid Extension!!")
        return

    fobj = open("Result.log","w")

    for FolderName, SubFolder, FileName in os.walk(DirName):
        for Fname in FileName:
            _, Ext = os.path.splitext(Fname)
            
            if(Ext == ExtName):
                fobj.write(Fname+"\n")

    fobj.close()

def main():
    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        print("Usage: Assignment30_01.py DirName .Extension")
        return
    
    FileSearch(sys.argv[1],sys.argv[2])
    


if __name__ == "__main__":
    main()