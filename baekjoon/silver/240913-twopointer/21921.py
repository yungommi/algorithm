#예상 시간복잡도 O(N) 

import sys
input = sys.stdin.readline
from collections import defaultdict 

def solution(N,K,A):
    answer = 0 
    start, end = 0, 0
    numberCount=defaultdict(int)
    sum = 0
    count = 0
    howmany = 1

    while end<N:
        if count >= K:
            sum -= A[start]
            start += 1 
            count -= 1
        else:
            sum += A[end]
            end += 1
            count += 1 
            if sum == answer:
                howmany += 1
            elif sum > answer:
                howmany = 1
                answer = sum 
            else:
                pass
    if answer == 0 :
        print("SAD")
    else:
        print(answer)
        print(howmany)

N,K = map(int, input().split())
A = list(map(int, input().split()))

solution(N,K,A)