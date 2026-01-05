def Multiply():
    iNo1 = 0
    iNo2 = 0

    print("Enter first number:")
    iNo1 = int(input())

    print("Enter second number:")
    iNo2 = int(input())

    return (iNo1 * iNo2)



def main():
    iRet = 0

    iRet = Multiply()

    print("Multiplication:",iRet)

if __name__ == "__main__":
    main()