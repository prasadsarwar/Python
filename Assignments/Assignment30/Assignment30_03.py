import sys
import os

###############################################
# option 1: read("\n") in loop
# option 2: readline() in loop
# option 3: readlines() then iterate the list of lines
###############################################

# option 4:


def DisplayLines(FName):
    Ret = os.path.exists(FName)
    if(Ret == False):
        print(f"{FName} does not exists")
        return
    
    fobj = open(FName,"r")

    for line in fobj:
        print(line,end="")

    fobj.close()

def main():

    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Usage: Assignment29_03.py File1.txt")
        return()
    
    DisplayLines(sys.argv[1])

if __name__ == "__main__":
    main()