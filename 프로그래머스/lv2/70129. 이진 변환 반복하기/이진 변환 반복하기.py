def solution(s):
    zeroDel = 0
    replaceCount = 0
    while(s != "1"):
        #주어진 문자열에서 0의 개수를 세고, 문자열에서 0을 모두 제거한다. 
        zeroCount = s.count("0")
        s = s.replace("0","")
        #0이 제거된 문자열의 길이 c를 2진수로 변환
        c = len(s)
        s = bin(c)[2:]
        #그 후 replaceCount를 1 증가시키고, zeroCount만큼 zeroDel에 더한다.
        replaceCount += 1
        zeroDel += zeroCount
    
    return [replaceCount,zeroDel]
        