# 예상 시간복잡도: O(N)

from collections import deque 

def solution(arr):
    d=deque(arr)
    answer = []
    tmp_1 = d.popleft()
    answer.append(tmp_1)
    while len(d)>0:
        tmp_2 = d.popleft()
        if tmp_1 == tmp_2:
            pass
        else:
            answer.append(tmp_2)
        tmp_1 = tmp_2
    return answer

