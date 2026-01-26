def Add(iNo1, iNo2):
    return (iNo1 + iNo2)

def main():
    iVal1 = 0
    iVal2 = 0
    iRet = 0

    print("Enter first number:")
    iVal1 = int(input())

    print("Enter second number:")
    iVal2 = int(input())

    iRet = Add(iVal1, iVal2)

    print("Addition:",iRet)
    

if __name__ == "__main__":
    main()