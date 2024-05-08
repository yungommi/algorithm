# 예상 시간복잡도: O(n)

def solution(my_string):
    answer = 0
    for x in my_string:
        if str.isdigit(x):
            answer += int(x)
    return answer


