class Numbers:

    def __init__(self, No):
        self.Value = abs(No)

    def CheckPrime(self):
        iEnd = (self.Value//2) + 1
        bFlag = True
        for iCnt in range(2,iEnd):
            if(self.Value%iCnt) == 0:
                bFlag = False
                break

        return bFlag
    
    def Factors(self):
        iEnd = (self.Value//2) + 1
        for iCnt in range(1,iEnd):
            if(self.Value%iCnt) == 0:
                print(iCnt,"\t",end="")

        print()

    def SumFactors(self):
        iEnd = (self.Value//2) + 1
        iSum = 0
        for iCnt in range(1,iEnd):
            if(self.Value%iCnt) == 0:
                iSum = iSum + iCnt
        return iSum
    
    def CheckPerfect(self):
        Res = self.SumFactors()

        return(Res == self.Value)

        
    
def main():
    obj1 = Numbers(12)
    print("Factors:")
    obj1.Factors()
    print("Prime:",obj1.CheckPrime())
    print("Summation of factors:",obj1.SumFactors())
    print("Perfect:",obj1.CheckPerfect())

    print("-"*30)

    obj2 = Numbers(13)
    print("Factors:")
    obj2.Factors()
    print("Prime:",obj2.CheckPrime())
    print("Summation of factors:",obj2.SumFactors())
    print("Perfect:",obj2.CheckPerfect())

    print("-"*30)

    obj3 = Numbers(6)
    print("Factors:")
    obj3.Factors()
    print("Prime:",obj3.CheckPrime())
    print("Summation of factors:",obj3.SumFactors())
    print("Perfect:",obj3.CheckPerfect())

if __name__ == "__main__":
    main()