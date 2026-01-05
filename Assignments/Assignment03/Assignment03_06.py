import sys

def main():
    Value = None

    print("Enter a value:")
    Value = input()

    print(type(Value))
    print("Address:",id(Value))
    print("Size:",sys.getsizeof(Value))

if __name__ == "__main__":
    main()