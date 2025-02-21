def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return None

'''def function(x,y):
    percent = int(y/x * 100)
  #  percent + 1 = (x+a +y-x) / x+a * 100 
  #  1 - (x-y)/x+a = percent+1 / 100
  # percent+1/100 <= 1-(x-y)/x+a < percent+2 /100 
'''
import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
def function(x,y):
  Z = (Y * 100) // X
  if Z >= 99:
      return(-1)
  else:
      answer = 0
      left = 1
      right = X
  
      while left <= right:
          mid = (left + right) // 2
          if (Y+mid)*100 // (X+mid) <= Z:
              left = mid+1
          else:
              answer = mid
              right = mid - 1
  
      return(answer)
  
print(function(X,Y))
