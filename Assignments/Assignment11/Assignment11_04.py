def ReverseNumber(iNo):
    iRev = 0
    
    iNo = abs(iNo) #updater

    while iNo != 0:
        iRev = iRev * 10 + (iNo % 10)
        iNo = iNo // 10

    return iRev

def main():
    iVal = 0
    iRet = 0

    print("Enter a number:")
    iVal = int(input())

    iRet = ReverseNumber(iVal)

    print("Reverse number is:", iRet)

if __name__ == "__main__":
    main()