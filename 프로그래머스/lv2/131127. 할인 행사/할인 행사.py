def solution(want, number, discount):
    answer = 0
    want_dict = dict()
    #원하는 품목이 모두 할인하는지 확인한 후 하나라도 없다면 0을 리턴
    for item in want:
        if item not in discount:
            return 0
        
    #반복문을 이용하여 원하는 품목과 수량을 딕셔너리 자료형으로 표현한다.
    for w,n in zip(want,number):
        want_dict[w] = n
        
    for i in range(len(discount) - 9):
        dict_temp = want_dict.copy()
        #해당 범위에 모든 품목이 다 있는지 체크
        for j in range(i,i + 10):
            if discount[j] in dict_temp and dict_temp[discount[j]] != 0:
                dict_temp[discount[j]] -= 1
            else:
                break
        #모든 품목이 다 있다면 answer +1
        if sum(dict_temp.values()) == 0:
            answer += 1
    return answer
            
    