# 예상 시간복잡도: O(n)

def solution(array):
    answer = 0
    for itm in array:
        tmp = str(itm).count('7')
        answer += tmp
    return answer

