def solution(k, tangerine):
    dict_type = {}
    answer = 0
    tangerine.sort()
    prevNum = tangerine[0]
    currentNum = 0
    # O(N) 복잡도로 각 크기별 개수 정보를 저장하고 있는 딕셔너리 생성
    for i, num in enumerate(tangerine):
        currentNum = num
        if i == 0:
            dict_type[num] = 1
            prevNum = num
        else:
            if prevNum == currentNum:
                dict_type[currentNum] += 1
            elif prevNum != currentNum:
                dict_type[currentNum] = 1
                prevNum = currentNum
    # 딕셔너리를 value값을 기준으로 내림차순으로 정렬
    dict_type = sorted(dict_type.items(), key = lambda item:item[1], reverse = True)
   
    # 정렬된 딕셔너리를 반복문을 통해 돌면서 k개를 달성하면 크기가 몇 종류인지 리턴해준다
    for value in dict_type:
        answer += 1
        k -= value[1]
        if k <= 0:
            return answer
    
    