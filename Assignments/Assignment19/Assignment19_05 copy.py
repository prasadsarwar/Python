from functools import reduce

ChkEven = lambda iNo: (iNo%2 == 0)
Square = lambda iNo: iNo * iNo
Add = lambda iNo1, iNo2: iNo1 + iNo2


def main():
    Data = list()
    iSize = 0

    print("Enter number of elements:")
    iSize = int(input())

    print(f"Enter {iSize} elements:")
    for _ in range(iSize):
        Data.append(int(input()))

    print("Input list:",Data)

    FData = list(filter(ChkEven, Data))
    print("List after filter:",FData)

    MData = list(map(Square, FData))
    print("List after map:",MData)

    RData = reduce(Add, MData)

    print("Output of reduce:",RData)

if __name__ == "__main__":
    main()