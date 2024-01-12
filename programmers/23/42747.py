# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    citations.sort()
    citations.reverse()
    i = 1
    while True:
        if citations[i-1] < i:
            return i-1
        elif i == len(citations):
            return i
        else:
            i += 1