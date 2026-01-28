import threading

def SumEvenFact(iNo):
    iEnd = (iNo//2) + 1
    iSum = 0

    for iCnt in range(2, iEnd,2):
        if(iNo % iCnt == 0):
            iSum = iSum + iCnt

    print("Summation of even factors:",iSum)

def SumOddFact(iNo):
    iEnd = (iNo//2) + 1
    iSum = 0

    for iCnt in range(1, iEnd,2):
        if(iNo % iCnt == 0):
            iSum = iSum + iCnt

    print("Summation of Odd factors:",iSum)
    


def main():
    iNo = 0

    print("Enter a number:")
    iNo = int(input())

    EvenFactor = threading.Thread(target=SumEvenFact, args=(iNo,))
    OddFactor = threading.Thread(target=SumOddFact, args=(iNo,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()
    print("Exit form main")

if __name__ == "__main__":
    main()