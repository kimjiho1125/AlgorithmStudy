def solution(k, ranges):
    answer = []
    ubak = [k]
    
    #정적분을 위한 좌표 구하기
    while(k > 1):
        #k가 짝수 일 때
        if k % 2 == 0:
            k = k//2
        else:
            k = k * 3 + 1
        ubak.append(k)
        
    #주어진 구간에 따라 정적분하기
    for r in ranges:
        total = 0
        ubakRange = ubak[r[0] : len(ubak)+r[1]]
        
        #시작점이 끝점보다 커서 유효하지 않을 때
        if r[0] >= len(ubak) + r[1]:
            answer.append(-1)
            continue
            
        #사다리꼴 높이 구하기 공식으로 정적분
        for i in range(len(ubakRange) - 1):
            total += (ubakRange[i] + ubakRange[i+1]) * 1 / 2
        
        answer.append(total)
    
    
    return answer