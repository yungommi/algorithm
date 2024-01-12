# 예상 시간복잡도: O(n)

def solution(emergency):
    answer = []
    e_s = sorted(emergency, reverse=True)
    for x in emergency:
        tmp = e_s.index(x)
        answer.append(tmp+1)
    return answer

