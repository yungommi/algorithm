# 예상 시간복잡도: O(n)

def solution(spell, dic):
    spell.sort()
    for itm in dic:
        if len(itm) == len(spell):
            l_ = list(itm)
            l_.sort()
            if spell == l_ :
                return 1
    return 2

