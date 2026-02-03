import sys
import os

def RenameFiles(DirName,Ext1,Ext2):
    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("Path does not exists")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    if((Ext1[0] != ".") or (Ext2[0] != ".")):
        print("Invalid Extension!!")
        return
    
    fobj = open("Result.log","w")
    
    for Folder, SubFolder, File in os.walk(DirName):
        for Fname in File:
            Name , Extionsion = os.path.splitext(Fname)
            
            if(Extionsion == Ext1):
                OldPath = os.path.join(Folder,Fname)

                NewName =  Name + Ext2
                NewPath = os.path.join(Folder,NewName)

                fobj.write("Renamed: "+OldPath+" to "+NewPath+"\n")

                os.rename(OldPath,NewPath)
    fobj.close()

def main():
    if(len(sys.argv) != 4):
        print("Invalid number of arguments")
        print("Usage: Assignment30_01.py DirName .Extension1 .Extension2")
        return
    
    RenameFiles(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
    main()