#예상 시간복잡도 O(?) 

import sys
input = sys.stdin.readline

N = int(input())
stone = [0] + list(map(int, input().split()))

start = 1 
end = (N-1) * (1+abs(stone[1]-stone[N]))
answer = (N-1) * (1+abs(stone[1]-stone[N]))

while start<=end:
    mid = (start + end)//2
    okay = False
    stack = [1]
    visited = [False] * (N+1)
    visited [1] = True
    while stack:
        p = stack.pop()
        if p==N:
            okay = True
        for i in range(p+1, N+1):
            if (i-p)*(1+abs(stone[p]-stone[i]))<=mid and not visited[i]:
                stack.append(i)
                visited[i] = True
    if okay:
        end = mid - 1
        answer = mid 
    else:
        start = mid + 1 

print(answer)