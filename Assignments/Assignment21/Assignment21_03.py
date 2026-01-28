import threading
import time

iCnt = 0
lobj = threading.Lock()

def Update():
    global iCnt

    for _ in range(40000000):
        with lobj:
            iCnt = iCnt + 1

def main():
    global iCnt
    

    thread1 = threading.Thread(target=Update)
    thread2 = threading.Thread(target=Update)

    start_time = time.time()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    end_time = time.time()
    
    print("Value of iCnt:",iCnt)

    print("total execution time:",(end_time-start_time))

if __name__ == "__main__":
    main()