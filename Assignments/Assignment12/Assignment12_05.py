def DisplayNumbers(iNo):

    iNo = abs(iNo)

    while(iNo > 0):
        print(iNo,"\t",end="")
        iNo = iNo - 1


def main():
    iVal = 0

    print("Enter a number:")
    iVal = int(input())

    DisplayNumbers(iVal)

if __name__ == "__main__":
    main()