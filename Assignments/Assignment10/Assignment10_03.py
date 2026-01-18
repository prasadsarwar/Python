def Factorial(iNo):
    iFact = 1

    if iNo < 0:
        iNo = -iNo

    for iCnt in range(2, (iNo+1)):
        iFact = iFact * iCnt

    return iFact


def main():

    iNum = 0
    iRet = 0

    print("Enter a number:")
    iNum = int(input())

    iRet = Factorial(iNum)

    print("Factorial is:", iRet)

if __name__ == "__main__":
    main()