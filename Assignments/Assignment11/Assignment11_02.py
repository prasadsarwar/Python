def CountDigits(iNo):
    iCount = 0

    if iNo == 0:
        return 1
    
    iNo = abs(iNo) #updater

    while iNo != 0:
        iCount = iCount + 1
        iNo = iNo // 10

    return iCount

def main():
    iVal = 0
    iRet = 0

    print("Enter a number:")
    iVal = int(input())

    iRet = CountDigits(iVal)

    # print(-3//10)

    print("Number of digits are:", iRet)

if __name__ == "__main__":
    main()