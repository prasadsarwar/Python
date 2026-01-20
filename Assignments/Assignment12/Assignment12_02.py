def DisplayFactors(iNo):

    iNo = abs(iNo)

    # for iCnt in range(1, iNo+1):
    #     if(iNo%iCnt) == 0:
    #         print(iCnt,"\t",end="")

    iEnd = (iNo//2)+1

    for iCnt in range(1, iEnd):
        if(iNo%iCnt) == 0:
            print(iCnt,"\t",end="")


def main():
    iVal = 0

    print("Enter a number:")
    iVal = int(input())

    DisplayFactors(iVal)



if __name__ == "__main__":
    main()