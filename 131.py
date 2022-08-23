n = int(input())
maxv, result = -1, -1
for i in range(1, n + 1):
    v, s = map(int, input().split())
    if s == 1 and v > maxv:
        maxv, result = v, i
print(result)
