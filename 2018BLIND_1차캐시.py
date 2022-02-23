from collections import deque

def solution(cacheSize, cities):
    cities = list(map(lambda x: x.upper(), cities))
    cache = deque([])
    answer = 0
    if cacheSize == 0:
        return len(cities)*5
    for city in cities:
        if city not in cache:
            if len(cache) == cacheSize:
                cache.popleft()

            cache.append(city)
            answer += 5

        else:
            cache.remove(city)
            cache.append(city)
            answer += 1

    return answer
