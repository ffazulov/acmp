n = int(input())
f = [int(c) for c in input()]
  
dd = ((0, 0), (0, 1), (1, 0), (1, 1))
  
d = [(0, 1)]
for i in range(1, n):
    cur = [-1, -1]
    for p, e in zip(dd, f):
        cur[e] = max(cur[e], d[i - 1][p[0]] + p[1])
    d.append((cur[0], cur[1]))
if d[-1][1] < 0:
    print("No solution")
else:
    e, result = 1, ""
    for i in range(n - 1, 0, -1):
        for k, p in enumerate(dd):
            if e == f[k] and d[i][e] == d[i - 1][p[0]] + p[1]:
                e = p[0]
                result += str(p[1])
                break
    result += str(e)
    print(result[::-1])
