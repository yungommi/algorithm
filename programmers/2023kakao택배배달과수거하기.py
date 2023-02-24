# 2023 kakao blind
# 택배 배달과 수거하기 

import math
def solution(cap, n, deliveries, pickups):
    answer = -1
    n = len(deliveries)
    d = [0]*n
    p = [0]*n
    x = 0
    for i in range(n-1,-1,-1):
        x += deliveries[i]
        if x > 0:
            d[i] = math.ceil(x/cap)
            x -= d[i]*cap
    x = 0
    for i in range(n-1,-1,-1):
        x += pickups[i]
        if x > 0:
            p[i] = math.ceil(x/cap)
            x -= p[i]*cap
    trip = 0
    for i in range(n-1,-1,-1):
        if d[i] > 0:
            trip += (i+1)
        
    print(d)
    print(p)
    return answer

print(solution(4,5,[1,0,3,1,2], [0,3,0,4,0]))
print(solution(2,7,[1,0,2,0,1,0,2], [0,2,0,1,0,2,0]))
print(solution(4,5,[1,0,3,1,6], [0,3,0,4,0]))

'''
def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0
    
    d = 0
    p = 0
    
    for i in range(n):
        d += deliveries[i]
        p += pickups[i]
        
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (n - i) * 2
    return answer
    '''