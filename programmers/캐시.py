from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = deque()
    for city in cities:
        city = city.lower()
        if city in q:
            q.remove(city)
            q.append(city)
            answer += 1
        else:
            q.append(city)

            if len(q) == cacheSize + 1:
                q.popleft()
            answer += 5

    return answer