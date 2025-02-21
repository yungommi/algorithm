#예상 시간복잡도 O(1) 

import sys
input = sys.stdin.readline

K = int(input())
x,y = map(int, input().split())
map = [[0]*(2**K) for _ in range(2**K)]
map[2**K-y][x-1] = -1

if K == 1 :
    for i in range(2):
        for j in range(2):
            if not map[i][j] :
                map[i][j]=1
else:
    cnt=0
    for i in range(0,2,1):
        for j in range(0,2,1):
            if not map[i][j] and cnt <3:
                map[i][j]=1
                cnt += 1
    cnt=0
    for i in range(0,2,1):
        for j in range(3,1,-1):
            if not map[i][j] and cnt <3:
                map[i][j]=2
                cnt += 1
    cnt=0
    for i in range(3,1,-1):
        for j in range(0,2,1):
            if not map[i][j] and cnt <3:
                map[i][j]=3
                cnt += 1
    cnt=0
    for i in range(3,1,-1):
        for j in range(3,1,-1):
            if not map[i][j] and cnt <3:
                map[i][j]=4
                cnt += 1
    cnt=0
    for i in range(1,3,1):
        for j in range(1,3,1):
            if not map[i][j]:
                map[i][j]=5

for row in map:
    for col in row:
        print(col, end=' ')
    print()

