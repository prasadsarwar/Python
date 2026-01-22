CheckOdd = lambda iNo : (iNo % 2 != 0)

def main():
    iVal = 0
    bRet = False

    print("Enter a number:")
    iVal = int(input())

    bRet = CheckOdd(iVal)

    print("Odd:",bRet)

if __name__ == "__main__":
    main()