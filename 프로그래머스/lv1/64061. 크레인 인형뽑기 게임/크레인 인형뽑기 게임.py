def solution(board, moves):
    answer = 0
    result = []
    
    for turn in moves:
        for i in range(len(board)):
            if board[i][turn-1] != 0:
                result.append(board[i][turn-1])
                board[i][turn-1] = 0
                break
                
    i = 0
    
    while i < len(result):
        if i == 0:
            i += 1
        else:
            if result[i-1] == result[i]:
                result.pop(i)
                result.pop(i-1)
                answer += 2
                i = 0
            else:
                i += 1
                
    return answer
    
    