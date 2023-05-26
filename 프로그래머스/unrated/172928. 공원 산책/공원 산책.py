def solution(park, routes):
    h = len(park)
    w = len(park[0])
    s = [0,0]
    breakPoint = 0
    # 시작 지점을 찾는다.
    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                s[0], s[1] = i, j
                breakPoint += 1
                break
        if breakPoint == 1:
            break
                
    for route in routes:
        direction, count = route.split();
        count = int(count)
        obstacleCheck = False
        if direction == "E" and s[1] + count < w:
            for i in range(1,count+1):
                if park[s[0]][s[1]+i]  == "X":
                    obstacleCheck = True
                    break
            if obstacleCheck == False:
                s[1] += count
        elif direction == "W" and s[1] - count > -1:
            for i in range(1,count+1):
                if park[s[0]][s[1]-i] == "X":
                    obstacleCheck = True
                    break
            if obstacleCheck == False:
                s[1] -= count
        elif direction == "S" and s[0] + count < h:
            for i in range(1,count+1):
                if park[s[0]+i][s[1]] == "X":
                    obstacleCheck = True
                    break
            if obstacleCheck == False:
                s[0] += count
        elif direction == "N" and s[0] - count > -1:
            for i in range(1,count+1):
                if park[s[0]-i][s[1]] == "X":
                    obstacleCheck = True
                    break
            if obstacleCheck == False:
                s[0] -= count
    return s