# 예상 시간복잡도: O(n)

def solution(start, end_num):
    answer = [i for i in range(end_num, start+1)]
    answer.reverse()
    return answer

