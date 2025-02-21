#예상 시간복잡도 O(N) 

import sys
input = sys.stdin.readline
from collections import defaultdict 

def solution(N,K,A):
    answer = 0 
    start, end = 0, 0
    numberCount=defaultdict(int)

    while end<N:
        if numberCount[A[end]] >= K:
            numberCount[A[start]] -= 1
            start += 1 
        else:
            numberCount[A[end]] += 1 
            end += 1
            answer = max(answer, end-start)
    return answer 

N,K = map(int, input().split())
A = list(map(int, input().split()))

print(solution(N,K,A))