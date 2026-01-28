import threading

def MaxElement(data):
    iMax = data[0]
    for element in data:
        if iMax < element:
            iMax = element

    print("Max:",iMax)

def MinElement(data):
    iMin = data[0]
    for element in data:
        if iMin > element:
            iMin = element

    print("Min:",iMin)

def main():
    iSize = 0
    data = list()

    print("Enter number of elements:")
    iSize = int(input())
     
    print(f"Enter {iSize} elements:")
    for iCnt in range(iSize):
        data.append(int(input()))

    t1 = threading.Thread(target=MaxElement,args=(data,))
    t2 = threading.Thread(target=MinElement,args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()