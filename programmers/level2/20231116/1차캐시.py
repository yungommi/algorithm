# 예상 시간 복잡도 O(n^2)

def solution(cacheSize, cities):
    if cacheSize == 0 :
        return 5*len(cities)
    ans = 0
    cache = []
    for c in cities:
        if c.upper() in cache: #cache hit
            ans += 1
            cache.pop(cache.index(c.upper()))
            cache.append(c.upper())
        else: #cache miss
            ans += 5 
            if len(cache)<cacheSize:
                cache.append(c.upper())
            else:
                cache.pop(0)
                cache.append(c.upper())
    return ans

