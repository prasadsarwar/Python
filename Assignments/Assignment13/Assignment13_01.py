def RectArea(fLength, fWidth):
    return (fLength * fWidth)

def main():

    fVal1 = 0.0
    fVal2 = 0.0
    fRet = 0.0

    print("Enter length:")
    fVal1 = float(input())

    print("Enter wodth:")
    fVal2 = float(input())

    fRet = RectArea(fVal1, fVal2)

    print(f"Area:{fRet}")


if __name__ == "__main__":
    main()