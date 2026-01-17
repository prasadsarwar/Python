def GetCube(iNo):

    # iAns = iNo * iNo * iNo
    # return iAns

    return (iNo ** 3)


def main():
    iVal = 0
    iRet = 0

    print("Enter a number:")
    iVal = int(input())

    iRet = GetCube(iVal)

    print("Cube is:", iRet)


if __name__ == "__main__":
    main()