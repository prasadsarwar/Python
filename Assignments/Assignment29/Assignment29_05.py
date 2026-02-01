import sys
import os

# def FindOccurance(FName, string):
#     iCount = 0

#     Ret = os.path.exists(FName)
#     if(Ret == False):
#         print(f"{FName} does not exists")
#         return
    
#     fobj = open(FName,"r")

#     Buffer = fobj.readlines()
    
#     for line in Buffer:
#         tline = line.split()
#         for token in tline:
#             if token == string:
#                 iCount = iCount + 1

#     return iCount


def FindOccurance(FName, string):
    iCount = 0

    Ret = os.path.exists(FName)
    if(Ret == False):
        print(f"{FName} does not exists")
        return
    
    fobj = open(FName,"r")

    Buffer = fobj.readline()
    
    while(len(Buffer) > 0):
        line = Buffer.split()

        for token in line:
            if(token == string):
                iCount = iCount + 1

        Buffer = fobj.readline()

    return iCount

def main():

    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        print("Usage: Assignment29_03.py File1.txt StringToFind")
        return()
    
    Ret = FindOccurance(sys.argv[1], sys.argv[2])

    print("Number of occurances:",Ret)


if __name__ == "__main__":
    main()