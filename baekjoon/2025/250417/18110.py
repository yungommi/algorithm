#예상시간복잡도 : O(N)

import sys
input = sys.stdin.readline 

def function(x):
    x_ = int(x)
    if x-x_ >= 0.5:
        return x_+1
    else:
        return x_

n = int(input())
if n==0:
    print(0)
    exit()

opi = [int(input()) for _ in range (n)]
opi.sort()
outlier = function(n*0.15)
opi = opi[outlier:n-outlier]
print(function(sum(opi)/len(opi)))

