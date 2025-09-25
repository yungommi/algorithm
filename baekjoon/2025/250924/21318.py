#예상시간복잡도 : O(NQ)

import sys
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

N = int(input())
arr = list(map(int, input().split()))
arr_ = [0]*(N+1)
for i in range(1,N):
  if arr[i-1]>arr[i]:
    arr_[i]=arr_[i-1]+1
  else:
    arr_[i]=arr_[i-1]
arr_[N] = arr_[N-1]
print(arr)
print(arr_)

Q=int(input())
for _ in range(Q):
    s,e = map(int, input().split())
    print(arr_[e-1]-arr_[s-1])
