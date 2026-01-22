# Min = lambda iNo1, iNo2 : min(iNo1, iNo2)

Min = lambda iNo1, iNo2 : iNo1 if iNo1 < iNo2 else iNo2


def main():
    iVal1 = 0
    iVal2 = 0
    iRet = 0

    print("Enter first number:")
    iVal1 = int(input())

    print("Enter second number:")
    iVal2 = int(input())

    iRet = Min(iVal1, iVal2)

    print("Min:",iRet)

if __name__ == "__main__":
    main()