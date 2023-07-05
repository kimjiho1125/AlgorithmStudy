from itertools import permutations

def solution(k, dungeons):
    maxCount = 0
    #최소 필요 피로도 기준으로 배열을 정렬
    dungeons.sort(key=lambda x:x[0],reverse=True)
    #탐험 불가능한 던전들 제외
    while True:
        if dungeons[0][0] > k:
            dungeons.pop(0)
        else:
            break
    
    #모든 방문 가능한 조합을 순열을 이용하여 생성
    pDungeons = []
    for i in permutations(dungeons,len(dungeons)):
        pDungeons.append(list(i))
    #완전 탐색을 통한 최대 던전 수 구하기
    i = 0
    while i < len(pDungeons):
        fatigue = k
        count = 0
        for j in pDungeons[i]:
            if fatigue >= j[0]:
                fatigue -= j[1]
                count += 1
            elif fatigue < j[0]:
                continue
        if maxCount < count:
            maxCount = count
        i += 1        
        
    return maxCount