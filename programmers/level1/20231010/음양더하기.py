# 예상 시간복잡도: O(N)

def solution(absolutes, signs):
    ans = 0 
    for i in range(len(absolutes)):
        if signs[i]:
            ans += absolutes[i]
        else:
            ans -= absolutes[i]
    return ans

