from functools import reduce

def main():
    Data = list()
    Fdata = list()
    iSize = 0
    
    print("Enter number of elements:")
    iSize = int(input())

    print("Enter elements:")
    for _ in range(iSize):
        Data.append(int(input()))

    Fdata = list(filter(lambda iNo: (iNo%2 == 0),Data))

    print("Data after filtering:\n",Fdata)
    # print("Number of even elements:",len(Fdata))

    Rdata = reduce(lambda count, _: count+1,Fdata,0)

    print(Rdata)

if __name__ == "__main__":
    main()
