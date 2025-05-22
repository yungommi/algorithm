#예상시간복잡도 : O(a*b)
import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip() 
a = len(A)
b = len(B)
LCS= [[""]*(b+1) for _ in range(a+1)] 

for i in range(1,a+1):
    for j in range(1,b+1):
        if A[i-1]==B[j-1]:
            LCS[i][j]=LCS[i-1][j-1]+A[i-1]
        else:
            if len(LCS[i-1][j])> len(LCS[i][j-1]):
                LCS[i][j]=LCS[i-1][j]
            else:
                LCS[i][j]=LCS[i][j-1]
ans = LCS[a][b]
if ans =='':
    print(0)
else:
    print(len(ans))
    print(ans)