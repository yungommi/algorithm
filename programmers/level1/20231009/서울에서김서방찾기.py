# 예상 시간복잡도: O(N)

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i]=='Kim':
            return f'김서방은 {i}에 있다'
        
        