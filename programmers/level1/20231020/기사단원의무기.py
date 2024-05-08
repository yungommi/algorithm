# 예상 시간복잡도: O(N^1.5)

def solution(number, limit, power):
    result = 0
    for i in range(1, number + 1):
        div_num = 0 
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                div_num += 2
        if i ** 0.5 % 1 == 0:
            div_num -= 1
        if div_num <= limit:
            result += div_num
        else:
            result += power
    return result
