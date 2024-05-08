# 예상 시간복잡도: O(n)

def solution(my_string, n):
    answer = ''
    for x in my_string:
        answer += x*n
    return answer

