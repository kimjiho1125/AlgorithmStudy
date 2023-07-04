from collections import deque

def solution(cacheSize, cities):
    time = 0
    cache = deque(maxlen=cacheSize)
    
    for city in cities:
        #대소문자 구분 X
        city = city.lower()

        if city in cache:
            time += 1
            cache.remove(city)
            cache.append(city)
        else:
            time +=5
            cache.append(city)
                    
    return time