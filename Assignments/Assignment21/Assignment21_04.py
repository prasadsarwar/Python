import threading

def SumElements(data,res_list):
    iSum = 0

    for element in data:
        iSum = iSum + element

    res_list[0] = iSum

def MultElements(data,res_list):
    iMult = 1

    for element in data:
        iMult = iMult * element

    res_list[0] = iMult


def main():
    iSize = 0
    data = list()
    result1 = [0]
    result2 = [0]

    print("Enter number of elements:")
    iSize = int(input())
     
    print(f"Enter {iSize} elements:")
    for iCnt in range(iSize):
        data.append(int(input()))

    t1 = threading.Thread(target=SumElements,args=(data,result1))
    t2 = threading.Thread(target=MultElements,args=(data,result2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Addition:",result1[0])
    print("Multiplication:",result2[0])


if __name__ == "__main__":
    main()