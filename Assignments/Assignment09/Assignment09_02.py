def CheckGreater(iNo1, iNo2):
    if iNo1 > iNo2:
        print(iNo1,"is greater")
    else:
        print(iNo2,"is greater")


def main():
    iVal1 = 0
    iVal2 = 0

    print("Enter first number:")
    iVal1 = int(input())

    print("Enter second number:")
    iVal2 = int(input())

    CheckGreater(iVal1,iVal2)

if __name__ == "__main__":
    main()