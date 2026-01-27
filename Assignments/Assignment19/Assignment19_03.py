from functools import reduce

PickRange = lambda iNo: iNo>=70 and iNo <=90
IncNum = lambda iNo: iNo + 10
Mult = lambda iNo1, iNo2: iNo1 * iNo2


def main():
    Data = list()
    iSize = 0

    print("Enter number of elements:")
    iSize = int(input())

    print(f"Enter {iSize} elements:")
    for _ in range(iSize):
        Data.append(int(input()))

    print("Input list:",Data)

    FData = list(filter(PickRange, Data))
    print("List after filter:",FData)

    MData = list(map(IncNum, FData))
    print("List after map:",MData)

    RData = reduce(Mult, MData)

    print("Output of reduce:",RData)

if __name__ == "__main__":
    main()