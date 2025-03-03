#예상 시간 복잡도 : O(N)

import sys
input = sys.stdin.readline 

n = int(input())
for _ in range(n):
    m ,st = input().split()
    ans = ''
    for x in st:
        ans += int(m)* x 
    print(ans)

