CheckDivsible = lambda iNo : (iNo % 5 == 0)

def main():
    iVal = 0
    bRet = False

    print("Enter a number:")
    iVal = int(input())

    bRet = CheckDivsible(iVal)

    print("Divisible by 5:",bRet)

if __name__ == "__main__":
    main()