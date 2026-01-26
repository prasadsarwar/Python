def Factorial(iNo):
    iNo = abs(iNo)
    iFact = 1

    while(iNo > 0):
        iFact = iFact * iNo
        iNo = iNo - 1
    
    return iFact

def main():
    iVal = 0

    print("Enter a number:")
    iVal = int(input())

    iRet = Factorial(iVal)

    print("Factorial:", iRet)

if __name__ == "__main__":
    main()