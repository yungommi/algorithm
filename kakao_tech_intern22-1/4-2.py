def solution(n, paths, gates, summits):
    field = {}
    answer = [-1, 10000001]

    for A, B, time in paths:
        for x, y in ((A, B), (B, A)):
            try:
                field[x].append((y, time))
            except:
                field[x] = [(y, time)]

    intensity = [10000001] * (n + 1)

    for gate in gates:
        intensity[gate] = 0

    check = set(summits)
    stack = gates

    while stack:
        target = set()

        while stack:
            now = stack.pop()

            for to, time in field[now]:
                max_time = max(intensity[now], time)

                if intensity[to] > max_time:
                    intensity[to] = max_time

                    if to not in check:
                        target.add(to)

        stack = list(target)

    return min([[summit, intensity[summit]] for summit in summits], key=lambda x: (x[1], x[0]))
