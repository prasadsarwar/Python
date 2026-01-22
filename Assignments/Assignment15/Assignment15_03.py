def main():
    Data = list()
    Fdata = list()
    iSize = 0
    
    print("Enter number of elements:")
    iSize = int(input())

    print("Enter elements:")
    for _ in range(iSize):
        Data.append(int(input()))

    Fdata = list(filter(lambda iNo: (iNo%2),Data))  #(iNo%2 == 0)

    print("Data after filtering:\n",Fdata)

if __name__ == "__main__":
    main()