class Arithmatic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
       print("Enter first number:")
       self.Value1 = int(input())

       print("Enter second number:")
       self.Value2 = int(input())

    def Addition(self):
        return (self.Value1 + self.Value2)
    
    def Subtraction(self):
        return (self.Value1 - self.Value2)
    
    def Multiplication(self):
        return (self.Value1 * self.Value2)
    
    def Division(self):
        iAns = 0.0

        try:
            iAns = self.Value1 / self.Value2
        except:
            print("Division by zero is not allowed")
    
        return iAns
        
    

def main():
    obj1 = Arithmatic()
    obj2 = Arithmatic()

    obj1.Accept()
    print("Addition:",obj1.Addition())
    print("Subtraction:",obj1.Subtraction())
    print("Multiplication:",obj1.Multiplication())
    print("Division:",obj1.Division())

    obj2.Accept()
    print("Addition:",obj2.Addition())
    print("Subtraction:",obj2.Subtraction())
    print("Multiplication:",obj2.Multiplication())
    print("Division:",obj2.Division())
    

if __name__ == "__main__":
    main()