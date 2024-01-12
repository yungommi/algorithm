# 예상 시간복잡도: O(n)

def solution(array):
    m = sorted(array)[-1]
    idx = array.index(m)
    answer = [m,idx]
    return answer

