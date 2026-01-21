def CheckPerfect(iNo):
    iSum = 0

    iNo = abs(iNo)

    for iCnt in range(1, (iNo//2)+1):
        
        if(iNo%iCnt) == 0:
            iSum = iSum + iCnt
        
    return (iSum == iNo)

def main():

    iVal1 = 0
    bRet = False

    print("Enter a number:")
    iVal1 = int(input())

    bRet = CheckPerfect(iVal1)

    if bRet == True:
        print("Perfect number")
    else:
        print("Not a perfect number")


if __name__ == "__main__":
    main()