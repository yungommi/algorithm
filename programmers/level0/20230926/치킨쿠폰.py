# 예상 시간복잡도: O(n)

def solution(chicken):
    answer = 0
    while chicken >= 10:
        div = chicken // 10
        mod = chicken % 10
        answer += div
        chicken = div+mod
    return answer
