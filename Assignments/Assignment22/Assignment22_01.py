class Demo:
    Value = 0

    def __init__(self,A,B):
        self.iNo1 = A
        self.iNo2 = B

    def Fun(self):
        print("Inside Fun")
        print("iNo1:",self.iNo1)
        print("iNo2:",self.iNo2)

    def Gun(self):
        print("Inside Gun")
        print("iNo1:",self.iNo1)
        print("iNo2:",self.iNo2)

def main():

    obj1 = Demo(11, 21)
    obj2 = Demo(51, 101)

    obj1.Fun()
    obj2.Fun()

    obj1.Gun()
    obj2.Gun()

if __name__ == "__main__":
    main()