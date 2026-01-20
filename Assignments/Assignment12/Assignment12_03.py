def Addition(iNo1, iNo2):
    return (iNo1 + iNo2)

def Subtraction(iNo1, iNo2):
    return (iNo1 - iNo2)

def Multiplication(iNo1, iNo2):
    return (iNo1 * iNo2)

def Division(iNo1, iNo2):

    if(iNo2 == 0):
        print("Cannot divide by zero")
        return
    
    return (iNo1 / iNo2)


def main():
    iVal1 = 0
    iVal2 = 0

    print("Enter first number:")
    iVal1 = int(input())

    print("Enter second number:")
    iVal2 = int(input())

    print("Addition:",Addition(iVal1, iVal2))
    print("Subtraction:",Subtraction(iVal1, iVal2))
    print("Multiplication",Multiplication(iVal1, iVal2))
    print("Division:",Division(iVal1, iVal2))


if __name__ == "__main__":
    main()