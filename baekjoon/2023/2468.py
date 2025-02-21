import sys
input = sys.stdin.readline 

n = int(input())
town = []
for _ in range(n):
    new = list(map(int, input().split()))
    tmp = [0]*n
    for i in range(n):
        if new[i]>n:
            tmp[i] = 1 
    town.append(tmp)
ans = 0 

print(town)