def ChkNum(iNo):
    if iNo == 0:
        print("Zero")
    elif iNo < 0:
        print("Negative")
    else:
        print("Positive")

def main():
    iVal = 0

    print("Enter a number:")
    iVal = int(input())

    ChkNum(iVal)

if __name__ == "__main__":
    main()