# 예상 시간복잡도: O(1)

def solution(number, n, m):
    if number%n ==0 and number%m ==0 :
        return 1
    else:
        return 0
    
