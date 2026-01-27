def Frequency(data, iKey):
    iCount = 0

    for iCnt in range(len(data)):
        if(data[iCnt] == iKey):
            iCount = iCount + 1

    return iCount

def main():
    Data = list()
    iNo = 0
    iSize = 0
    iRet = 0

    print("Enter number of elements:")
    iSize = int(input())

    print(f"Enter {iSize} elements:")
    for _ in range(iSize):
        Data.append(int(input()))

    print("Enter element to find:")
    iNo = int(input())
    
    iRet = Frequency(Data, iNo)

    print("Frequency:",iRet)

if __name__ == "__main__":
    main()