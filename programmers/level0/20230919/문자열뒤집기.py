# 예상 시간복잡도: O(n)

def solution(my_string, s, e):
    answer = ''
    answer += my_string[0:s]
    tmp = []
    for i in range(s,e+1):
        tmp.append(my_string[i])
    tmp.reverse()
    answer += "".join(tmp)
    answer += my_string[e+1:]
    return answer

