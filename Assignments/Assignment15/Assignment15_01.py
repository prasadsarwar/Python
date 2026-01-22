def main():
    Data = list()
    Mdata = list()
    iSize = 0
    
    print("Enter number of elements:")
    iSize = int(input())

    print("Enter elements:")
    for _ in range(iSize):
        Data.append(int(input()))

    Mdata = list(map(lambda iNo: iNo*iNo,Data))

    print("Data after mapping:\n",Mdata)

if __name__ == "__main__":
    main()