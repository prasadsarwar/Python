import sys
import os
import shutil

def CopyFiles(DirName,NewDirName,Ext):
    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("Path does not exists")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    if(Ext[0] != "."):
        print("Invalid Extension!!")
        return

    
    for Folder, SubFolder, File in os.walk(DirName):
        for Fname in File:
            _, extn = os.path.splitext(Fname)
            
            if(extn == Ext):
                OldPath = os.path.join(Folder,Fname)
                rel_path = os.path.relpath(Folder,DirName)
                NewPath = os.path.join(NewDirName,rel_path)

                os.makedirs(NewPath,exist_ok=True)
                shutil.copy2(OldPath, NewPath)

def main():
    if(len(sys.argv) != 4):
        print("Invalid number of arguments")
        print("Usage: Assignment30_01.py ExistingDirName NewDirName .extension")
        return
    
    CopyFiles(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
    main()