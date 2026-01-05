def main():
    iNo1 = 10
    iNo2 = 10

    print(id(iNo1))     #same id(address)
    print(id(iNo2))     #same id(address)

    listA = [10, 20, 30]     
    listB = [10, 20, 30]     

    print(id(listA))    #different id(address)
    print(id(listB))    #different id(address)

if __name__ == "__main__":
    main()