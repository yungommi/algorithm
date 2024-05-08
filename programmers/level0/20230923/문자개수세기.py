# 예상 시간복잡도: O(n)

def solution(my_string):
    answer = [0 for i in range(52)]
    for s in my_string:
        if s.isupper(): 
            k = 65
        else: 
            k = 71
        answer[ord(s)-k] += 1
    return answer

