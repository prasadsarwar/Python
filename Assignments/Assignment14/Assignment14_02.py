Cube = lambda iNo : (iNo * iNo * iNo) # iNo ** 3

def main():
    iVal = 0
    iRet = 0

    print("Enter a number:")
    iVal = int(input())

    iRet = Cube(iVal)

    print("Cube:",iRet)

if __name__ == "__main__":
    main()