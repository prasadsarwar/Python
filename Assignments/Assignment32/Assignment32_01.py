import sys
import os
import hashlib


def CalculateChecksum(FileName):
    fobj = open(FileName,"rb")
    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def DirectoryFilesChecksum(DirName):
    
    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("Directory not exists")
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    fobj = open("Result.log","w")
    fobj.write("File Name \tChecksum\n")


    for Folder, Subfolder, File in os.walk(DirName):
        for Fname in File:
            Fname = os.path.join(Folder,Fname)
            CheckSum = CalculateChecksum(Fname)
            fobj.write(Fname+"\t"+CheckSum+"\n")

    fobj.close()

def main():
    if(len(sys.argv) != 2):
        print("Invalid number of argumants")
        print("Usage: Assignment32_01.py DirectoryName")
        return
    
    DirectoryFilesChecksum(sys.argv[1])


if __name__ == "__main__":
    main()