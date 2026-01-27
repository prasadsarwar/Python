def MaxElement(data):
    iMax = data[0]

    for iCnt in range(1,len(data)):
        if(iMax < data[iCnt]):
            iMax = data[iCnt]
    return iMax

def main():
    Data = list()
    iSize = 0
    iRet = 0

    print("Enter number of elements:")
    iSize = int(input())

    print(f"Enter {iSize} elements:")
    for _ in range(iSize):
        Data.append(int(input()))

    iRet = MaxElement(Data)

    print("Max:",iRet)

if __name__ == "__main__":
    main()