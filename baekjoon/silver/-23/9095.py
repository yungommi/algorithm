# 9095 
# dp 

cache = [0] * 11
cache[1] = 1
cache[2] = 2
cache[3] = 4
for i in range(4,11):
    cache[i] = sum(cache[i-3:i])

n = int(input())
for i in range(n):
    x = int(input())
    print(cache[x])