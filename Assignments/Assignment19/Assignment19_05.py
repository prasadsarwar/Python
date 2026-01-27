from functools import reduce

def CheckPrime(iNo):
    for iCnt in range(2,(iNo//2)+1):
        if iNo%iCnt == 0:
            return False
        
    return True
    

Mult = lambda iNo: iNo * 2
Max = lambda iNo1, iNo2: iNo1 if iNo1 > iNo2 else iNo2


def main():
    Data = list()
    iSize = 0

    print("Enter number of elements:")
    iSize = int(input())

    print(f"Enter {iSize} elements:")
    for _ in range(iSize):
        Data.append(int(input()))

    print("Input list:",Data)

    FData = list(filter(CheckPrime, Data))
    print("List after filter:",FData)

    MData = list(map(Mult, FData))
    print("List after map:",MData)

    RData = reduce(Max, MData)

    print("Output of reduce:",RData)

if __name__ == "__main__":
    main()