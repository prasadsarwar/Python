def GetSquare(iNo):

    # iAns = iNo * iNo
    # return iAns

    return (iNo * iNo)


def main():
    iVal = 0
    iRet = 0

    print("Enter a number:")
    iVal = int(input())

    iRet = GetSquare(iVal)

    print("Square is:", iRet)


if __name__ == "__main__":
    main()