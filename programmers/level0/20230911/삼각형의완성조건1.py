# 예상 시간복잡도: O(n)

def solution(sides):
    sides.sort()
    if sides[2]<sides[0]+sides[1]:
        return 1
    else:
        return 2
    
    