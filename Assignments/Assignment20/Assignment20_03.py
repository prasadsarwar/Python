import threading

def SumEven(Data):
    iSum = 0

    for Element in  Data:
        if Element % 2 == 0:
            iSum = iSum + Element

    print("Summation of even elements:",iSum)

def SumOdd(Data):
    iSum = 0

    for Element in  Data:
        if Element % 2 != 0:
            iSum = iSum + Element

    print("Summation of odd elements:",iSum)
    
def main():
    iSize = 0
    Data = list()

    print("Enter number of elements:")
    iSize = int(input())

    print(f"Enter {iSize} elements:")
    for iCnt in range(iSize):
        Data.append(int(input()))

    EvenList = threading.Thread(target=SumEven, args=(Data,))
    OddList = threading.Thread(target=SumOdd, args=(Data,))

    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join()
    print("Exit form main")

if __name__ == "__main__":
    main()