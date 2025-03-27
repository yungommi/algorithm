#예상시간복잡도 : O(NlogN)

import sys
input = sys.stdin.readline
import copy

n = int(input())
X = list(map(int,input().split()))
S = list(set(X))
S.sort() 
dict= {S[i]:i for i in range(len(S))}

for x in X:
    print(dict[x], end=' ')
