# 시간복잡도 O(N)

import sys 
input = sys.stdin.readline 

n = int(input())
root = list(map(int, input().split()))
item = int(input())
def delete(node):
    root[node] = -10
    for i in range(n):
        if root[i] == node:
            delete(i)

delete(item)

ans = 0 
for i in range(n):
    if i not in root and root[i] > -2:
        ans += 1 
print(ans)