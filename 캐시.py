from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)

    if cacheSize == 0:
        return len(cities) * 5

    for c in cities:
        print(cache)
        c = c.lower()
        if c in cache:  # 캐시에 있는 데이터라면
            answer += 1
            cache.remove(c)  # 데이터 삭제
        else:  # 캐시에 없는 데이터라면
            answer += 5
        cache.append(c)

    return answer


print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
      "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
