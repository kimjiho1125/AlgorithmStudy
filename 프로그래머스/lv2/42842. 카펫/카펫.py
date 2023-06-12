def solution(brown, yellow):
    #총 카펫의 크기
    size = brown + yellow
    
    for side in range(size+1,1,-1):
        #한 변의 길이가 될 수 있는 수 구하기
        if size%side == 0:
            anotherSide = size/side
            if (side-2)*(anotherSide-2) == yellow:
                return [side,anotherSide]