#예상시간복잡도 : O(N)

import sys
input = sys.stdin.readline

N= int(input())

arr = list(map(int,input().split()))
arr.sort()
ans = 0
for i in range(N):
    ans += (N-i)*arr[i]

print(ans)

