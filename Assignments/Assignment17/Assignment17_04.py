def Factorial(iNo):
    iNo = abs(iNo)
    iSum = 0
    iEnd = (iNo // 2)+1

    for iCnt in range(1, iEnd):
        if iNo % iCnt == 0:
            iSum = iSum + iCnt
    
    return iSum

def main():
    iVal = 0

    print("Enter a number:")
    iVal = int(input())

    iRet = Factorial(iVal)

    print("Factorial:", iRet)

if __name__ == "__main__":
    main()