def MinElement(data):
    iMin = data[0]

    for iCnt in range(1,len(data)):
        if(iMin > data[iCnt]):
            iMin = data[iCnt]
    return iMin

def main():
    Data = list()
    iSize = 0
    iRet = 0

    print("Enter number of elements:")
    iSize = int(input())

    print(f"Enter {iSize} elements:")
    for _ in range(iSize):
        Data.append(int(input()))

    iRet = MinElement(Data)

    print("Min:",iRet)

if __name__ == "__main__":
    main()