# 예상 시간복잡도: O(n)

def solution(my_string):
    answer = ''
    for x in my_string:
        if x in "aeiou":
            pass
        else:
            answer += x
    return answer

