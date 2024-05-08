# 예상 시간복잡도: O(n)

def solution(names):
    result = []
    for k in range(0,len(names),5):
        result.append(names[k])
    return result

