# 예상 시간복잡도: O(a^3 * b)

def solution(myString, pat):
    if pat.lower() in myString.lower():
        return 1
    else:
        return 0
    
