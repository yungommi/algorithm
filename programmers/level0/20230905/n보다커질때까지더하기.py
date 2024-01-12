# 예상 시간복잡도: O(n)

def solution(numbers, n):
    sum = 0
    for i in numbers:
        if sum +i <= n:
            sum += i 
        else:
            return sum+i
        
