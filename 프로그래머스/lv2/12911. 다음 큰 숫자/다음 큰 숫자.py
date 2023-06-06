def solution(n):
    binN = bin(n)
    oneCount = binN.count('1') 
    while True:
        n += 1
        binN = bin(n)
        compareOneCount = binN.count('1') 
        if oneCount == compareOneCount:
            return n
