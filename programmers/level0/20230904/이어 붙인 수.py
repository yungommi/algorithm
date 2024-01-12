# 예상 시간복잡도: O(n)

def solution(num_list):
    odd, even = "", ""
    for x in num_list:
        if x%2 == 1:
            odd += str(x)
        else:
            even += str(x)
    return int(odd)+int(even)

