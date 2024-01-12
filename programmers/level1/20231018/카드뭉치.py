# 예상 시간복잡도: O(N)

from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    tmp1 = cards1.popleft()
    tmp2 = cards2.popleft()
    for x in goal:
        if x == tmp1:
            if cards1:
                tmp1 = cards1.popleft()
            else:
                tmp1 = ''
        elif x == tmp2:
            if cards2:
                tmp2 = cards2.popleft()
            else:
                tmp2 = ''
        else:
            return 'No'
    return 'Yes'


