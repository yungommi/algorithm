# https://school.programmers.co.kr/learn/courses/30/lessons/43238
  
  
def solution(n, times):
    answer = 0
    left, right = 1, times[0] * n
    while left <= right:
      mid = (left+ right) // 2
      people = 0
      for time in times:
        people += mid // time
        if people >= n:
          break
            
      if people >= n:
        answer = mid
        right = mid - 1
      elif people < n:
        left = mid + 1              
      return answer
 