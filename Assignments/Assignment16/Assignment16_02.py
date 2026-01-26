def ChkNum(iNo):
    return (iNo%2 == 0)

def main():
    iVal = 0
    bRet = False

    print("Enter a number:")
    iVal = int(input())

    bRet = ChkNum(iVal)

    if bRet == True:
        print("Even number")
    else:
        print("Odd number")

if __name__ == "__main__":
    main()