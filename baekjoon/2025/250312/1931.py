#예상시간복잡도 : O(nlogn) 

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
l = [0]*n
for i in range(n):
    l[i] = list(map(int,input().split()))

l.sort(key=lambda x: (x[1],x[0]))
#print(l)
qu = deque(l)
endtime = 0 
ans = 0 
while qu:
    tmp = qu.popleft()
    if endtime <= tmp[0]:
        endtime = tmp[1]
        ans += 1 
        #print(tmp)
print(ans)
