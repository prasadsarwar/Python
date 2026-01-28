import threading

def CountUpperCase(sText):
    iCnt = 0

    for ch in sText:
        if((ch >= "A") and (ch <= 'Z')):
            iCnt = iCnt + 1
    print("Number of upper case characters:",iCnt)

def CountLowerCase(sText):
    iCnt = 0

    for ch in sText:
        if((ch >= "a") and (ch <= 'z')):
            iCnt = iCnt + 1
    print("Number of lower case characters:",iCnt)

def CountDigits(sText):
    iCnt = 0

    for ch in sText:
        if((ch >= "0") and (ch <= '9')):
            iCnt = iCnt + 1
    print("Number of digits:",iCnt)
    
def main():
    sName = ""

    print("Enter string:")
    sName = input()

    Small = threading.Thread(target=CountUpperCase,args=(sName,))
    Capital = threading.Thread(target=CountLowerCase,args=(sName,))
    Digits = threading.Thread(target=CountDigits,args=(sName,))

    Small.start()
    Capital.start()
    Digits.start()

    Small.join()
    Capital.join()
    Digits.join()


if __name__ == "__main__":
    main()