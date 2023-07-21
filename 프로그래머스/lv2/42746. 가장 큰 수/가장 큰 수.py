def solution(numbers):
    # numbers = list(map(str,numbers))
    # result = list()
    # for i in range(len(numbers)):
    #     temp = numbers[i]
    #     while len(temp) < 4:
    #         temp += temp
    #     result.append([temp, numbers[i]])
    # result.sort(reverse = True)
    # answer = str(int("".join(r[1] for r in result)))   
    # return answer
    
    # 더 좋은 풀이
    # numbers 배열의 숫자들을 문자열로 변경
    numbers = list(map(str, numbers))
    # 실제 크기에 상관 없이 가장 높은 자리 수의 크기를 기준으로 정렬
    # x3하는 이유는 numbers에 들어가는 원소의 최대 크기가 천단위이기 때문
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    return str(int(''.join(numbers)))
    
   