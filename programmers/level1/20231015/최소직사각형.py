# 예상 시간복잡도: O(N)

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

