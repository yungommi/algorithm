#예상시간복잡도 : O(n C m )

import sys
input = sys.stdin.readline

n = int(input())
s = set()
for i in range(n):
    inp = input().rstrip()
    l = len(inp)
    s.add((l,inp))
ans = list(s)
ans.sort() 

for a,b in ans:
    print(b)