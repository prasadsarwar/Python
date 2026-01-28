import threading

def DisplayPrime(Data):
    iEnd = 0
    iCnt = 0
    for element in Data:
        iEnd = (element // 2) + 1

        for iCnt in range(2,iEnd):
            if element%iCnt == 0:
                break
        if (iCnt == (iEnd-1) or element == 2 or element == 3) :
            print(element,"\t",end="")

    print()

def DisplayNonPrime(Data):
    iEnd = 0
    iCnt = 0
    for element in Data:
        iEnd = (element // 2) + 1

        for iCnt in range(2,iEnd):
            if element%iCnt == 0:
                print(element,"\t",end="")
                break

    print()
def main():
    iSize = 0
    data = list()

    print("Enter number of elements:")
    iSize = int(input())
     
    print(f"Enter {iSize} elements:")
    for iCnt in range(iSize):
        data.append(int(input()))

    Prime = threading.Thread(target=DisplayPrime,args=(data,))
    NonPrime = threading.Thread(target=DisplayNonPrime,args=(data,))

    print("Prime numbers:")
    Prime.start()
    Prime.join()

    print("Non Prime numbers:")
    NonPrime.start()
    NonPrime.join()


if __name__ == "__main__":
    main()