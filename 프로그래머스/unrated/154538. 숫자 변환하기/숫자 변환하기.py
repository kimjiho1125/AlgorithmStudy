def solution(x, y, n):
    # y+1인 이유는 직관적으로 인덱스와 값을 일치시키기 위해서임
    memorized = [1e9] * (y+1)
    memorized[x] = 0
    
    for i in range(x,y+1):
        if memorized[i] == 1e9:
            continue
        if i + n <= y:
            memorized[i+n] = min(memorized[i+n],memorized[i] + 1)
        if i * 2 <= y:
            memorized[i*2] = min(memorized[i*2],memorized[i] + 1)
        if i * 3 <= y:
            memorized[i*3] = min(memorized[i*3],memorized[i] + 1)
    
    if memorized[y] == 1e9:
        return -1
    
    return memorized[y] 