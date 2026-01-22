Max = lambda iNo1, iNo2, iNo3 : max(iNo1, iNo2, iNo3)

def main():
    iVal1 = 0
    iVal2 = 0
    iVal3 = 0
    iRet = 0

    print("Enter first number:")
    iVal1 = int(input())

    print("Enter second number:")
    iVal2 = int(input())

    print("Enter third number:")
    iVal3 = int(input())

    iRet = Max(iVal1, iVal2, iVal3)

    print("Greatedt number:",iRet)

if __name__ == "__main__":
    main()