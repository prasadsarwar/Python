from sys import getsizeof

def main():
    iNo1 = 11
    iNo2 = hash(iNo1)

    print(iNo2)             #11 same value
    print(hash(iNo2))       #11 same value

    sVal = "Prasad Sarwar"
    listA = [10,20,30]
    tupleA = (10,20,30)
    fNo = 10.11
    nDemo = None

    print(hash(sVal))   #hash value
    # print(hash(listA))    #error
    print(hash(tupleA))    #hash value
    print(hash(fNo))    #hash value
    print(hash(nDemo))  #hash value

    

if __name__ == "__main__":
    main()