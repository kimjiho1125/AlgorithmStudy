def solution(clothes):
    answer = 0
    clothe_dict = dict()
    for clothe in clothes:
        if clothe[1] not in clothe_dict:
            clothe_dict[clothe[1]] = 1
        elif clothe[1] in clothe_dict:
            clothe_dict[clothe[1]] += 1
    
    if len(clothe_dict) == 1:
        answer = sum(clothe_dict.values())
    
    if len(clothe_dict) > 1:
        temp = 1
        for value in clothe_dict.values():
            temp *= (value + 1)
        answer += (temp - 1)
        
    return answer