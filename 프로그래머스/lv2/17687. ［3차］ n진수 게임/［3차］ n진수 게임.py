#10진수 -> n진수 변환
def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n,base)
    return convert_notation(q,base) + T[r] if q else T[r]

def solution(n, t, m, p):
    answer = ""
    temp = ""
    num = 0
    #0~ n진법으로 변환한 문자열 만들기
    while len(temp) < t*m:
        temp += convert_notation(num,n)
        num += 1

    for i in range(len(temp)):
        if (i+1) == p and (i+1) <= t*m:
            answer += temp[i]
            p += m
    return answer