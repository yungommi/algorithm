# 예상 시간 복잡도 O(n)

def solution(clothes):
    clothing = {}
    for x in clothes:
        if x[1] in clothing:
            clothing[x[1]] +=1
        else:
            clothing[x[1]] = 1
    answer = 1
    for x in clothing:
        answer = answer * (clothing[x]+1)
    return (answer - 1)

