import os

def SearchFile(FName):
    Ret = os.path.exists(FName)

    return Ret


def main():
    FileName = ""

    print("Enter file name you want to search:")
    FileName = input()

    Ret = SearchFile(FileName)

    if(Ret == True):
        print("File exists")
    else:
        print("File does not exists")


if __name__ == "__main__":
    main()