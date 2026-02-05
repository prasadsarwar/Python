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


def FindDuplicate(DirName):
    
    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("Directory not exists")
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return

    Duplicate = {}

    for Folder,_ , File in os.walk(DirName):
        for Fname in File:
            Fname = os.path.join(Folder,Fname)
            CheckSum = CalculateChecksum(Fname)
            
            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(Fname)
                # print(Fname)
            else:
                Duplicate[CheckSum] = [Fname]

    return Duplicate

def DisplayDuplicate(DupDict):
    fobj = open("Result.log","w")
    Border = "-"*50

    Result = list(filter(lambda lst: len(lst)>1, DupDict.values()))
    
    Count = 0
    for value in Result:
        Count = 0
        for fName in value:
            fobj.write(fName+"\n")
            Count = Count + 1
        
        fobj.write(str(Count)+"\n")
        fobj.write(Border+"\n")
        # print(len(Value))

    fobj.close()

def main():
    if(len(sys.argv) != 2):
        print("Invalid number of argumants")
        print("Usage: Assignment32_01.py DirectoryName")
        return
    
    Ret = FindDuplicate(sys.argv[1])
    DisplayDuplicate(Ret)


if __name__ == "__main__":
    main()