#예상시간복잡도 : O(logN)
import sys
input = sys.stdin.readline

s,c = map(int, input().split())
L = [int(input()) for _ in range(s)]

start = 1 
end = max(L) 

tmp = 0

while start <= end :
    mid = (start+end)//2 
    cnt = sum(pa//mid for pa in L)
    if cnt >= c :
        tmp = max(tmp, mid) 
        start = mid + 1 
    else:
        end = mid - 1 

ans = sum(L) - c*tmp 
print(ans)