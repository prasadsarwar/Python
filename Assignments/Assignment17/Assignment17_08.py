def DisplayPattern(iNo):
    iNo = abs(iNo)
    
    for iCnt in range(iNo):
        for jCnt in range(iNo):  
            if jCnt <= iCnt:
                print(jCnt+1,"\t",end="")
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