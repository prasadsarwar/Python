def SumDigits(iNo):
    iNo = abs(iNo)
    iSum = 0
    
    while(iNo > 0):
        iSum = iSum + (iNo%10)
        iNo = iNo // 10

    return iSum

def main():
    iVal = 0

    print("Enter a number:")
    iVal = int(input())

    iRet = SumDigits(iVal)

    print("Addition of digits:",iRet)

if __name__ == "__main__":
    main()