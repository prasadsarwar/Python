def DisplayEven(iNo):

    if iNo < 0:
        iNo = -iNo
        
    for iCnt in range(2, (iNo+1), 2):
        print(iCnt,"\t",end="")


def main():

    iNum = 0

    print("Enter a number:")
    iNum = int(input())

    DisplayEven(iNum)

if __name__ == "__main__":
    main()