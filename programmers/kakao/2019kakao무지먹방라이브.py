# 2019 kakao blind 
# 무지의 먹방 라이브 

from itertools import accumulate

def solution(food_times, k):
    n = len(food_times)
    if n > k : return k + 1
    food_acc = list(accumulate((f := sorted(food_times))))
    for i in range(n) :
        if food_acc[i] + (n-(i+1))*f[i] > k :
            remain_food = [index+1 for index, food in enumerate(food_times) if food >= f[i]]
            idx = (k - (food_acc[i-1] + (n-i)*f[i-1])) % (n-i)
            return remain_food[idx]
    return -1