# 예상 시간복잡도: O(n^3)

def solution(myString, pat):
    new = ""
    for x in myString:
        if x == "A":
            new += "B"
        else:
            new += "A"
    return int(pat in new)

