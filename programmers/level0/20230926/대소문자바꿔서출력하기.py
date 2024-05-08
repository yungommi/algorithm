# 예상 시간복잡도: O(n)

str = input()
ans = ''
for x in str:
    if x.isupper():
        ans += x.lower()
    else:
        ans += x.upper()
        
print(ans)

