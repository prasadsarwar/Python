def DisplayTable(iNo):
    for iCnt in range(1, 11):
        print((iNo*iCnt),"\t",end="")


def main():

    iNum = 0

    print("Enter a number:")
    iNum = int(input())

    DisplayTable(iNum)

if __name__ == "__main__":
    main()