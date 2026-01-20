def DisplayNumbers(iNo):

    iNo = abs(iNo)

    for iCnt in range(1, iNo+1):
        print(iCnt,"\t",end="")


def main():
    iVal = 0

    print("Enter a number:")
    iVal = int(input())

    DisplayNumbers(iVal)

if __name__ == "__main__":
    main()