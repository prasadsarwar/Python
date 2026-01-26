def DisplayPattern(iNo):
    iNo = abs(iNo)
    
    for _ in range(iNo):
        for _ in range(iNo):  
            print("*\t",end="")

        print()

def main():
    iVal = 0

    print("Enter a number:")
    iVal = int(input())

    DisplayPattern(iVal)

if __name__ == "__main__":
    main()