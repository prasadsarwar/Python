def Addition(iNo1, iNo2):
    iAns = 0
    iAns = iNo1 + iNo2
    return iAns

def Subtraction(iNo1, iNo2):
    iAns = 0
    iAns = iNo1 - iNo2
    return iAns

def Multiplication(iNo1, iNo2):
    iAns = 0
    iAns = iNo1 * iNo2
    return iAns

def Division(iNo1, iNo2):
    fAns = 0.0

    if iNo2 == 0:
        print("Cant divide by zero")
        return

    iAns = iNo1 / iNo2
    return iAns


def main():
    iVal1 = 0
    iVal2 = 0

    print("Enter first number:")
    iVal1 = int(input())

    print("Enter second number:")
    iVal2 = int(input())

    print("Addition:", Addition(iVal1,iVal2))
    print("Subtraction:", Subtraction(iVal1,iVal2))
    print("Multiplication:", Multiplication(iVal1,iVal2))
    print("Division:", Division(iVal1,iVal2))

main()