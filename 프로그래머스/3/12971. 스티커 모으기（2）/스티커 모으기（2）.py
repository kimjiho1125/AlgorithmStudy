def solution(sticker):
    dp1 = [0] * len(sticker)
    dp2 = [0] * len(sticker)
    
    if len(sticker) == 1:
        return sticker[0]
    
    #첫번째 스티커를 뽑았을 경우 -> 마지막 스티커 고려X
    dp1[0], dp1[1] = sticker[0], max(sticker[0], sticker[1])
    for i in range(2, len(sticker) - 1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
    
    #첫번째 스티커를 뽑지 않았을 경우 -> 마지막 스티커 고려
    dp2[0], dp2[1] = 0, max(0, sticker[1])
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
    
    return max(dp1[len(sticker)-2],dp2[len(sticker)-1])