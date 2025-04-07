#예상시간복잡도 : O(N)

import sys
input = sys.stdin.readline
from collections import deque

A,B = map(int,input().split())
def function(A,B):
    q = deque([(A,1)])
    while q:
        now,step = q.popleft()
        for tmp in [now*2, 10*now+1]:
            if tmp == B:
                return step+1
            if tmp<B:
                q.append((tmp,step+1))
    return -1 

print(function(A,B))
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
=======
>>>>>>> Stashed changes




def solution(S,A):
    N=len(A)
    dic = {i:[] for i in range(N)}
    for i in range(1,N):
        dic[i].append(A[i])
        dic[A[i]].append(i)
    ans = [0]*N 

    def dfs (node,prev):
        longest = 1 
        for k in dic[node]:
            if k == prev:
                continue
            if S[k]!=S[node]:
                tmp = 1+dfs(k,S[node])
                longest = max(longest,tmp)
        return longest 

    for i in range(N):
        ans[i]=dfs(i,'')
<<<<<<< Updated upstream
    return max(ans)
>>>>>>> Stashed changes
=======
    return max(ans)
>>>>>>> Stashed changes
