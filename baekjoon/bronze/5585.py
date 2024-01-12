# 5585
# greedy 

n = int(input())

def function(n:int):
    answer = 0
    n = 1000 - n
    answer += n // 500
    n = n % 500 
    answer += n // 100
    n = n % 100
    answer += n // 50 
    n = n % 50 
    answer += n // 10 
    n = n % 10 
    answer += n // 5 
    n = n % 5 
    answer += n 
    return answer

print(function(n))