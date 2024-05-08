# 예상 시간복잡도: O(n)

def solution(n, control):
    alp_num = {
        "w" : 1,
        "s" : -1,
        "d" : 10,
        "a" : -10
              }

    for alp in control:
        n += alp_num[alp]
    return n

