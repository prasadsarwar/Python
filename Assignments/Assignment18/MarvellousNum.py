def CheckPrime(iNo):
    for iCnt in range(2,(iNo//2)+1):
        if iNo%iCnt == 0:
            return False
        
    return True
    