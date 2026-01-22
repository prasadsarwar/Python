# Max = lambda iNo1, iNo2 : max(iNo1, iNo2)

Max = lambda iNo1, iNo2 : iNo1 if iNo1 > iNo2 else iNo2


def main():
    iVal1 = 0
    iVal2 = 0
    iRet = 0

    print("Enter first number:")
    iVal1 = int(input())

    print("Enter second number:")
    iVal2 = int(input())

    iRet = Max(iVal1, iVal2)

    print("Max:",iRet)

if __name__ == "__main__":
    main()