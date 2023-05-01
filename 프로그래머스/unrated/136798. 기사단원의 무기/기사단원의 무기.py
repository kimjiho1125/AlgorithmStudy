def numberOfDivisor(n):
    count = 0
    for i in range(1,int(n**(1/2)) + 1):
        if n % i == 0:
            if (i**2) == n:
                count += 1
            else:
                count += 2
    return count

def solution(number, limit, power):
    answer = 0
    for num in range(1,number+1):
        if numberOfDivisor(num) > limit:
            answer += power
        else:
            answer += numberOfDivisor(num)
    return answer