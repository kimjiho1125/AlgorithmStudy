from collections import deque

def solution(cacheSize, cities):
    time = 0
    cache = deque(maxlen=cacheSize)
    #maxlen 설정시 maxlen 이상의 값을 추가할 경우 맨 왼쪽 원소가 삭제되고, 값이      들어간다! 
    
    for city in cities:
        #대소문자 구분 X
        city = city.lower()

        if city in cache:
            time += 1
            #LRU 알고리즘에 의해 캐시 순서 최신화
            cache.remove(city)
            cache.append(city)
        else:
            time +=5
            cache.append(city)
                    
    return time