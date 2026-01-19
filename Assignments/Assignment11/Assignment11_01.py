def CheckPrime(iNo):
    bFlag = True

    if iNo < 0:
        iNo = - iNo

    for iCnt in range(2,iNo):
        if iNo % iCnt == 0:
            bFlag = False
            break

    return bFlag

def main():
    iVal = 0
    bRet = False

    print("Enter a number:")
    iVal = int(input())

    bRet = CheckPrime(iVal)

    if bRet == True:
        print("Prime number")
    else:
        print("Composite number")

if __name__ == "__main__":
    main()