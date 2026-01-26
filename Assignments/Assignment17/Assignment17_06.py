def DisplayPattern(iNo):
    iNo = abs(iNo)
    
    for i in range(iNo):
        for j in range(iNo):  
            if(j < (iNo - i)):
                print("*\t",end="")
            else:
                print("\t",end="")
        print()

def main():
    iVal = 0

    print("Enter a number:")
    iVal = int(input())

    DisplayPattern(iVal)

if __name__ == "__main__":
    main()