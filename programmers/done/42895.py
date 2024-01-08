# https://school.programmers.co.kr/learn/courses/30/lessons/42895 

def solution(N, number):
    made = [set() for x in range(9)]
    if number == N:
        return 1 
    made[1].add(N)
    for i in range(2,9): # i = 4
        made[i].add(int(str(N)*i))
        for m in range(1,i): # m : 1 2 3 
            for x in made[m]: # x : 1 2 3 
                for y in made[i-m]: # y : 3 2 1 
                    made[i].add(x+y)
                    made[i].add(x-y)
                    made[i].add(x*y)
                    if y != 0 :
                        made[i].add(x//y)
        if number in made[i]:
            return i
    return -1