from collections import deque

def solution(cacheSize, cities):
    answer = 0
    #빈 deque 만들기
    cache = deque()
    if cacheSize > 0:
        for city in cities:
            #대소문자 구분 X
            city = city.lower()

            if len(cache) > 0:
                if city in cache:
                    answer += 1
                    cache.remove(city)
                    cache.append(city)
                elif city not in cache:
                    answer += 5
                    if len(cache) == cacheSize:
                        cache.popleft()
                        cache.append(city)
                    elif len(cache) < cacheSize:
                        cache.append(city)
            elif len(cache) == 0:
                answer += 5
                cache.append(city)
    elif cacheSize == 0:
        answer = len(cities) * 5
            
    return answer