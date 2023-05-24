def solution(wallpaper):
    lux = 50
    luy = 50
    rdx = 0
    rdy = 0
    
    for i, items in enumerate(wallpaper):
        for j, item in enumerate(items):
            if item == "#":
                if lux > i:
                    lux = i
                if luy > j:
                    luy = j
                if rdx < i+1:
                    rdx = i+1
                if rdy < j+1:
                    rdy = j+1
    
    return [lux,luy,rdx,rdy] 
    
    