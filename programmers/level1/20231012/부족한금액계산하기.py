# 예상 시간복잡도: O(1)

def solution(price, money, count):
    p = price * (1+count)*count//2
    return max(0,p-money)

