#예상시간복잡도 : O(N)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

l = [] 
while True:
    try:
        inp = int(input().rstrip())
        l.append(inp)
    except:
        break

def function(arr):
    if not arr:
        return 
    mid = arr[0]
    tmpL = []
    idx = len(arr)
    for i in range(1,len(arr)):
        if arr[i]>mid:
            idx = i
            break
    tmpL = arr[1:idx]
    tmpR = arr[idx:]
    function(tmpL)
    function(tmpR)
    print(mid)
function(l)
