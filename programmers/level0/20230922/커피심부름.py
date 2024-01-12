# 예상 시간복잡도: O(n)

def solution(order):
    am = ["iceamericano", "americanoice","hotamericano", "americanohot","americano","anything"]
    answer = 0
    for x in order:
        if x in am:
            answer += 4500
        else:
            answer += 5000   
    return answer

