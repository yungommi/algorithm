# 예상 시간복잡도: O(N)

def solution(lottos, win_nums):
    lotto = {6 : 1, 5 : 2, 4 : 3, 3 : 4, 2 : 5, 1 : 6, 0 : 6}
    zero = lottos.count(0)
    correct = len( set(lottos) & set(win_nums) )
    best= correct + zero
    worst= correct
    result = [lotto[best], lotto[worst]]
    return result

