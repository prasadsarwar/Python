def ReverseNumber(iNo):
    iRev = 0
    
    iNo = abs(iNo) #updater

    while iNo != 0:
        iRev = iRev * 10 + (iNo % 10)
        iNo = iNo // 10

    return iRev

def CheckPalindrome(iNum):
    iRev = ReverseNumber(iNum)

    if abs(iNum) == iRev:
        return True
    else:
        return False
    

def main():
    iVal = 0
    bRet = False

    print("Enter a number:")
    iVal = int(input())

    bRet = CheckPalindrome(iVal)

    print("Palindrome:", bRet)

if __name__ == "__main__":
    main()