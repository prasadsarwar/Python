def main():
    Data = list()
    Fdata = list()
    iSize = 0
    
    print("Enter number of elements:")
    iSize = int(input())

    print("Enter elements:")
    for _ in range(iSize):
        Data.append(input())

    Fdata = list(filter(lambda Val: (len(Val) > 5),Data))  

    print("Data after filtering:\n",Fdata)

if __name__ == "__main__":
    main()