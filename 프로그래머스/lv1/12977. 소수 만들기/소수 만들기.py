def isPrime(x):
    for i in range(2,int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
        
def solution(nums):
    answer = 0
    nums.sort()
    numbers = []
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                numbers.append(nums[i]+nums[j]+nums[k])
    for number in numbers:
        if isPrime(number):
            answer += 1
    return answer
    
        