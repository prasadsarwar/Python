class BankAccount:
    ROI = 10.5

    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount


    def Display(self):
        print("Account holder name:",self.Name)
        print("Current balance:",self.Amount)

    def Deposite(self,money):
        self.Amount = self.Amount + money

    def Withdraw(self,money):
        if(money <= self.Amount):
            self.Amount = self.Amount - money
        else:
            print("Insufficient balance!!!")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100

        return Interest
    
def main():
    obj1 = BankAccount("Prasad",1000000)
    obj1.Display()
    obj1.Deposite(100000)
    obj1.Display()
    obj1.Withdraw(10000)
    obj1.Display()
    Res = obj1.CalculateInterest()
    print("Interest:",Res)

    print("-"*30)

    obj1 = BankAccount("Omkar",20000)
    obj1.Display()
    obj1.Deposite(5000)
    obj1.Display()
    obj1.Withdraw(10000)
    obj1.Display()
    Res = obj1.CalculateInterest()
    print("Interest:",Res)

if __name__ == "__main__":
    main()