def Summation(iNo):
    iSum = 0

    if iNo < 0:
        iNo = -iNo

    for iCnt in range(1, (iNo+1)):
        iSum = iSum + iCnt

    return iSum


def main():

    iNum = 0
    iRet = 0

    print("Enter a number:")
    iNum = int(input())

    iRet = Summation(iNum)

    print("Summation is:", iRet)

if __name__ == "__main__":
    main()