def main():
    
    listA = [10, 20, 30]     
    tupleA = (10, 20, 30)  
    setA = {10,20,30}
    dictA = {"name":"Prasad", "Age":"20", "City":"Pune"}   
    name = "Prasad"
    iNo = 10
    fNo = 10.20

    print(len(listA))   #3
    print(len(tupleA))  #3
    print(len(setA))    #3
    print(len(dictA))   #3
    print(len(name))    #6
    print(len(iNo))     #error
    print(len(fNo))     #error

if __name__ == "__main__":
    main()