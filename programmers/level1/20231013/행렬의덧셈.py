# 예상 시간복잡도: O(N) ?? numpy 시간복잡도를모르겟다..

import numpy
def solution(arr1, arr2):
    a=numpy.array(arr1)
    b=numpy.array(arr2)
    result=a+b
    return result.tolist()
