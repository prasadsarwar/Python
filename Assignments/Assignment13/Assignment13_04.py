def BinaryEquivalent(iNo):
    iAns = 0
    iPlace = 1

    while(iNo > 0):
        iDigit = iNo % 2
        iAns = iAns + (iDigit * iPlace)
        iNo = iNo // 2
        iPlace = iPlace * 10

    return iAns


def main():

    iVal1 = 0
    iRet = 0

    print("Enter a number:")
    iVal1 = int(input())

    iRet = BinaryEquivalent(iVal1)

    print(f"Binary of {iVal1} is: {iRet}")


if __name__ == "__main__":
    main()