def CheckPrime(iNo):
    iNo = abs(iNo)
    bFlag = True
    
    for iCnt in range(2, iNo):
        if iNo % iCnt == 0:
            bFlag = False
            break
    
    return bFlag

def main():
    iVal = 0

    print("Enter a number:")
    iVal = int(input())

    bRet = CheckPrime(iVal)

    if bRet == True:
        print("It is prime number")
    else:
        print("it is composite number")

if __name__ == "__main__":
    main()