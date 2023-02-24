# https://school.programmers.co.kr/learn/courses/30/lessons/42746

# 처음 시도한 풀이 - 시간초과 
'''def solution(numbers):
    answer = ''
    real = [str(x) for x in numbers]
    n = [str(x)*4 for x in numbers]
    N =[int(x[:4]) for x in n]
    while len(N) != 0:
        m = N.index(max(N))
        answer += real[m]
        del real[m]
        del N[m]

    return answer'''

# 답지 봄 
def solution(numbers):
    numbers_str = [str(num) for num in numbers]                
    numbers_str.sort(key=lambda num: num*3, reverse=True)       

    return str(int(''.join(numbers_str)))