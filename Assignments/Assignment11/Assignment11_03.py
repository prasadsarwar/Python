def SumDigits(iNo):
    iSum = 0
    
    iNo = abs(iNo) #updater

    while iNo != 0:
        iSum = iSum + (iNo % 10)
        iNo = iNo // 10

    return iSum

def main():
    iVal = 0
    iRet = 0

    print("Enter a number:")
    iVal = int(input())

    iRet = SumDigits(iVal)

    print("Summation of digits is:", iRet)

if __name__ == "__main__":
    main()