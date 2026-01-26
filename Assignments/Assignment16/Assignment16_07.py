def CheckDividible(iNo):
    return (iNo%5 == 0)

def main():
    iVal = 0
    bRet = False

    print("Enter a number:")
    iVal = int(input())

    bRet = CheckDividible(iVal)

    print(bRet)
    # if bRet == True:
    #     print("Divisible by 5")
    # else:
    #     print("Not divisible by 5")

if __name__ == "__main__":
    main()