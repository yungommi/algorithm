# 1700 
# greedy 

def function(N,K,arr):
  count = 0
  plugins = []
  
  for i in range(K) :
    if arr[i] in plugins:
      continue

    if len(plugins) < N :
      plugins.append(arr[i])
      continue
    
    after_use_index = []
    remains = arr[i:]
    
    for j in range(N) :
      if plugins[j] not in remains :
        after_use_index.append(101) 
          # remain에 없으면 101번째 뒤에 사용한다 가정, for문 탈출후 바로 사용 
        continue

      after_use_index.append(remains.index(plugins[j]))
      # remain에 있으면 remain에서 plugins[j]가 몇번째로 사용되는지 보고 가장 늦게 사용되는 item 사용 

    plug_out_index = after_use_index.index(max(after_use_index))
    del plugins[plug_out_index]
    plugins.append(arr[i])
    count += 1
  return count

print(function(3,7,[2,3,2,3,1,2,7]))

'''N,K = map (int, input().split())
arr = list(map(int,input().split()))

print(function(N,K,arr))'''