def DisplayGrade(iMarks):

    if iMarks < 0 or iMarks > 100:
        print("Invalid marks")
        return

    if iMarks < 50:
        print("Fail")
    elif iMarks < 60:
        print("Second class")
    elif iMarks < 75:
        print(" First class")
    elif iMarks <= 100:
        print("Distinction")


def main():

    iVal1 = 0

    print("Enter a number:")
    iVal1 = int(input())

    DisplayGrade(iVal1)

if __name__ == "__main__":
    main()