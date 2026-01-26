from Arithmatic import Add, Sub, Mult, Div

def main():
    iVal1 = 0
    iVal2 = 0
    iRet = 0

    print("Enter first number:")
    iVal1 = int(input())

    print("Enter second number:")
    iVal2 = int(input())

    print("Addition:",Add(iVal1,iVal2))
    print("Subtraction:",Sub(iVal1,iVal2))
    print("Multiplication:",Mult(iVal1,iVal2))
    print("Division:",Div(iVal1,iVal2))

if __name__ == "__main__":
    main()