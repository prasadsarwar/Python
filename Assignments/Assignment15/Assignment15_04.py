from functools import reduce

def main():
    Data = list()
    Rdata = 0
    iSize = 0
    
    print("Enter number of elements:")
    iSize = int(input())

    print("Enter elements:")
    for _ in range(iSize):
        Data.append(int(input()))

    Rdata = reduce(lambda iNo1, iNo2: (iNo1 + iNo2),Data)

    print("Result after reduce:",Rdata)

if __name__ == "__main__":
    main()