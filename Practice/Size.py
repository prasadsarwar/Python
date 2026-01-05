from sys import getsizeof

def main():
    
    listA = [10, 20, 30]     
    tupleA = (10, 20, 30)  
    setA = {10,20,30}
    dictA = {"name":"Prasad", "Age":"20", "City":"Pune"}   
    name = "Prasad"
    iNo = 10
    fNo = 10.20

    #size may vary depending on system
    
    print(getsizeof(listA))   #88
    print(getsizeof(tupleA))  #72
    print(getsizeof(setA))    #216
    print(getsizeof(dictA))   #184
    print(getsizeof(name))    #47
    print(getsizeof(iNo))     #28
    print(getsizeof(fNo))     #24

if __name__ == "__main__":
    main()