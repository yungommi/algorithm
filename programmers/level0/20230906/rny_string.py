# 예상 시간복잡도: O(n)

def solution(rny_string):
    ans = ''
    for x in rny_string:
        if x == "m":
            ans += "rn"
        else:
            ans+=x
    return ans

