keyPads = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]

def findCoord(target):
    for x in range(len(keyPads)):
        for y in range(3):
            if keyPads[x][y] == target:
                return x,y
            
def solution(numbers,hand):
    answer = ""
    left = (3,0)
    right = (3,2)
    
    for number in numbers:
        if number in [1,4,7]:
            left = findCoord(number)
            answer += "L"
        elif number in [3,6,9]:
            right = findCoord(number)
            answer += "R"
        else:
            target_x, target_y = findCoord(number)
            fromLeftToTarget = abs(left[0] - target_x) + abs(left[1] - target_y)
            fromRightToTarget = abs(right[0] - target_x) + abs(right[1] - target_y)
            if fromLeftToTarget < fromRightToTarget:
                left = target_x, target_y
                answer += "L"
            elif fromLeftToTarget > fromRightToTarget:
                right = target_x, target_y
                answer += "R"
            else:
                if hand == "left":
                    left = target_x, target_y
                    answer += "L"
                else:
                    right = target_x, target_y
                    answer += "R"
    return answer      