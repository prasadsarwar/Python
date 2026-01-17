def CheckDivisible(iNo):
    
    if((iNo % 3 == 0) and (iNo % 5 == 0)):
        return True
    else:
        return False


def main():
    iVal = 0
    bRet = False

    print("Enter a number:")
    iVal = int(input())

    bRet = CheckDivisible(iVal)

    if bRet == True:
        print(iVal, "is divisible by both 3 and 5")
    else:
        print(iVal, "is not divisible by both 3 and 5")


if __name__ == "__main__":
    main()