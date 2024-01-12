# 예상 시간복잡도: O(n)

def solution(my_string, is_suffix):
    suff = []
    for i in range(len(my_string)):
        suff.append(my_string[i:])
    return int(is_suffix in suff)

