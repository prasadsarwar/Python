from MarvellousNum import CheckPrime

def ListPrime(data):
    iSum = 0

    for iCnt in range(len(data)):
        if CheckPrime(data[iCnt]):
            iSum = iSum + data[iCnt]
            print(data[iCnt],"\t",end="")

    return iSum

def main():
    Data = list()
    iSize = 0
    iRet = 0

    print("Enter number of elements:")
    iSize = int(input())

    print(f"Enter {iSize} elements:")
    for _ in range(iSize):
        Data.append(int(input()))

    iRet = ListPrime(Data)

    print("Addition:",iRet)

if __name__ == "__main__":
    main()