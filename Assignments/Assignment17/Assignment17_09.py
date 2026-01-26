def CountDigits(iNo):
    iNo = abs(iNo)
    iCnt = 0
    
    while(iNo > 0):
        iCnt = iCnt + 1
        iNo = iNo // 10

    return iCnt

def main():
    iVal = 0

    print("Enter a number:")
    iVal = int(input())

    iRet = CountDigits(iVal)

    print("Number of digits:",iRet)

if __name__ == "__main__":
    main()