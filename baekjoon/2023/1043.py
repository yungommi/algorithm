import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trues = set(list(map(int, input().split()))[1:])
party = []
cnt = []

for _ in range(m):
    data = set(map(int, input().split()[1:]))
    if data:
        party.append(data)
        cnt.append(1)

for _ in range(m):
    for i, p in enumerate(party):
        if trues & p:
            cnt[i] = 0
            trues |= p #bitwise operator a |= b => a = (a | b)

print(sum(cnt))

