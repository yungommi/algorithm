# 예상 시간 복잡도 : O(n)? O(1)? 

import numpy as np
def solution(num_list, n):
    tmp = np.array(num_list).reshape(-1,n)
    return tmp.tolist()

