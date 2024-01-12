# 예상 시간복잡도: O(n)

def solution(my_string, alp):
    answer = ''
    for x in my_string:
        if alp == x:
            answer += x.upper()
        else:
            answer += x
    return answer





    
