#예상시간복잡도 : O(N)

import sys 
input = sys.stdin.readline 

N = int(input())
def isprime(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    for i in range(2,n):
        if n%i == 0 :
            return 0
    return 1

l = list(map(int,input().split()))
ans = 0 
for x in l:
    ans += isprime(x)

print(ans)
