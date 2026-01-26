def Display(iNo):
    iNo = abs(iNo)
    
    for _ in range(iNo):
        print("*\t",end="")

def main():
    iVal = 0

    print("Enter a number:")
    iVal = int(input())

    Display(iVal)

if __name__ == "__main__":
    main()