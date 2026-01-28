import threading

def Display():
    for iCnt in range(1,51):
        print(iCnt)

def DisplayReverse():
    for iCnt in range(50,0,-1):
        print(iCnt)

def main():

    Thread1 = threading.Thread(target=Display)
    Thread2 = threading.Thread(target=DisplayReverse)
    
    Thread1.start()
    Thread1.join()
    
    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()