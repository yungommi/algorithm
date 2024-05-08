# 예상 시간복잡도: O(N^2)

import itertools
def solution(numbers):
    tmp = itertools.combinations(numbers,2)
    ans = []
    for x in tmp:
        ans.append(sum(x))
    ans = list(set(ans))
    ans.sort()
    return ans

