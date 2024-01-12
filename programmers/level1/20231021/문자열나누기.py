# 예상 시간복잡도: O(N)

def solution(s):
    first_alp = "" 
    s_count = 0 
    d_count = 0 
    result = 0 
    for alp in s:
        if first_alp == "":
            first_alp = alp
            s_count = 1
            continue
        if first_alp == alp:
            s_count += 1
        else:
            d_count += 1
        if s_count == d_count:
            first_alp = ""
            s_count = 0
            d_count = 0
            result += 1
    if first_alp != "":
        result += 1  
    return result

    