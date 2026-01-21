def CircleArea(fRadius):
    return (3.14 *fRadius * fRadius)

def main():

    fVal1 = 0.0
    fRet = 0.0

    print("Enter radius:")
    fVal1 = float(input())

    fRet = CircleArea(fVal1)

    print(f"Area:{fRet}")


if __name__ == "__main__":
    main()