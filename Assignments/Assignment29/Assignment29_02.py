import os

def DisplayFileContents(FName):
    Ret = os.path.exists(FName)

    if(Ret == False):
        print("File does not exists")
        return
    
    fobj = open(FName, "r")

    Buffer = fobj.read()

    print(Buffer)

    fobj.close()

def main():
    FileName = ""

    print("Enter file name you want to search:")
    FileName = input()

    DisplayFileContents(FileName)
    


if __name__ == "__main__":
    main()