import threading

def DisplayEven():
    for iCnt in range(1,11):
        print(iCnt*2,"\t", end="")

def DisplayOdd():
    for iCnt in range(1,11):
        print((iCnt*2)-1,"\t", end="")

def main():
    Even = threading.Thread(target=DisplayEven)
    Odd = threading.Thread(target=DisplayOdd)

    Even.start()
    print()
    Odd.start()

    Even.join()
    Odd.join()


if __name__ == "__main__":
    main()