# 예상 시간 복잡도 : O(n) 


def solution(intStrs, k, s, l):
    answer = []
    for x in intStrs:
        tmp = int(x[s:s+l])
        if tmp>k:
            answer.append(tmp)
    return answer

