Square = lambda iNo : (iNo * iNo)

def main():
    iVal = 0
    iRet = 0

    print("Enter a number:")
    iVal = int(input())

    iRet = Square(iVal)

    print("Square:",iRet)

if __name__ == "__main__":
    main()