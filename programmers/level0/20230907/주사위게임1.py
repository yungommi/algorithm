# 예상 시간복잡도: O(1)

def solution(a, b):
    if (a*b) % 2 == 1 :
        return a**2 + b**2
    elif a%2==0 and b%2==0:
        return max(a-b, b-a)
    else:
        return 2 * ( a + b )
    
