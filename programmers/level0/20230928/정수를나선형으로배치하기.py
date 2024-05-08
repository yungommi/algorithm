# 예상 시간복잡도: O(n^2)

def solution(n):
    sprial = [[0] * n for _ in range(n)]  
    dx = [1,0,-1,0] 
    dy = [0,1,0,-1]
    x, y = 0, 0
    diretion = 0
    for i in range(1,(n*n)+1):
        sprial[y][x] = i
        nx = x + dx[diretion]
        ny = y + dy[diretion]
        if nx >= n or nx < 0 or ny >= n or ny < 0 or sprial[ny][nx] != 0:
            diretion = (diretion + 1) % 4
            nx = x + dx[diretion]
            ny = y + dy[diretion]
        x, y = nx, ny
    return sprial

