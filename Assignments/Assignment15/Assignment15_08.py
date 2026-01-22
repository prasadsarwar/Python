def main():
    Data = list()
    Fdata = list()
    iSize = 0
    
    print("Enter number of elements:")
    iSize = int(input())

    print("Enter elements:")
    for _ in range(iSize):
        Data.append(int(input()))

    Fdata = list(filter(lambda iNo: (iNo%3 == 0 and iNo%5 == 0),Data)) #iNo %15

    print("Data after filtering:\n",Fdata)

if __name__ == "__main__":
    main()