q = {i: 0 for i in range(10)}
n, m = map(int, input().split())
for i in range(1, n+1):
    for j in range(1, m+1):
        d = i*j
        while d:
            r =d % 10
            if r in q:
                q[r] += 1
            d //=10
for i in range(10):
    print(q[i])
