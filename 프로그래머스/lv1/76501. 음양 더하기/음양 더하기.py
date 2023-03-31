def solution(absolutes, signs):
    # answer = 0
    # for i in range(len(absolutes)):
    #     if(signs[i]):
    #         answer += absolutes[i]
    #     else:
    #         answer -= absolutes[i]
    # return answer
    # 더 좋은 풀이
    return sum(absolute if sign else -absolute for absolute,sign in zip(absolutes,signs))