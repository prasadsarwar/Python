# def CheckVowel(cVal):

#     cVal = cVal.lower()

#     if(cVal == "a" or cVal == "e" or cVal == "i" or cVal == "o" or cVal == "u"):
#         return True
#     else:
#         return False

def CheckVowel(cVal):
    cVal = cVal.lower()

    Vowel_list = ("a","e","i","o","u")

    if cVal in Vowel_list:
        return True
    else:
        return False
        
def main():
    cVal = ""
    bRet = False

    print("Enter an alphabet:")
    cVal = input()[0]

    bRet = CheckVowel(cVal)

    if bRet == True:
        print(cVal,"is vowel")
    else:
        print(cVal,"is not a vowel")

if __name__ == "__main__":
    main()