# 예상 시간복잡도: O(xy)

def solution(wallpaper):
    x_ = len(wallpaper)
    y_ = len(wallpaper[0])
    x_min, y_min = x_,y_
    x_max, y_max = 0, 0
    for x in range(x_):
        for y in range(y_):
            if wallpaper[x][y]=='#':
                x_min = min(x_min, x)
                y_min = min(y_min, y)
                x_max = max(x_max, x+1)
                y_max = max(y_max, y+1)
    answer = [x_min,y_min,x_max,y_max]
    return answer

