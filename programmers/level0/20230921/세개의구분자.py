# 예상 시간복잡도: O(n)

import re

def solution(myStr):
    answer = re.sub("[a-c]", " ", myStr).split()
    return answer if len(answer) > 0 else ["EMPTY"]


