# 예상 시간복잡도: O(N!)

import itertools 
def solution(number):
    answer = 0 
    ans = itertools.combinations(number,3)
    for x in ans:
        if sum(x)==0:
            answer += 1
    return answer 

