import sys

nums = sys.stdin.readline().rstrip()
splits = nums
for i in range(1,4):
    tmp = splits[0:i]  
    min_num = tmp  
    while splits and splits[:len(tmp)] == tmp: 
             splits = splits[len(tmp):]  
             tmp = str(int(tmp)+1)  
    if not splits:  #splits 모두 씀=> print 
        break
    splits = nums #for문으로 다시 넘어감, split reset 
print(min_num, int(tmp)-1)
