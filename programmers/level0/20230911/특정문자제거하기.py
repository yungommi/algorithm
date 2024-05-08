# 예상 시간복잡도: O(n)

def solution(my_string, letter):
    answer = ''
    for x in my_string:
        if x==letter:
            pass
        else:
            answer += x
    return answer

