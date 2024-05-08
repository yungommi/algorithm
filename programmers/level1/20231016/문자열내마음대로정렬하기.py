# 예상 시간복잡도: O(N)

def solution(strings, n):
    answer = []
    for x in strings:
        tmp = [x[n], x]
        answer.append(tmp)
    answer.sort()
    return [ x[1] for x in answer]

