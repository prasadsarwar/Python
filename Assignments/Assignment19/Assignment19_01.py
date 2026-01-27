Pwr = lambda iNo: iNo ** 2

def main():
    iVal1 = 0
    iRet = 0

    print("Enter a number:")
    iVal1 = int(input())

    iRet = Pwr(iVal1)

    print(iRet)

if __name__ == "__main__":
    main()