def solution(numbers, target):
    
    #DFS와 재귀를 활용한 풀이
    def calc(index, sum):
        nonlocal answer
        
        if index == len(numbers):
            if sum == target:
                answer += 1
            return
        calc(index+1, sum + numbers[index])
        calc(index+1, sum - numbers[index])
    
    answer = 0
    calc(0,0)
    
    return answer