n, k1, k2, s = map(int, input().split())
a = [[0 for _ in range(n+1)] for _ in range(n+1)]
a[k1][k2] = 1 << 100;
for i1 in range(k1, n):
    for i2 in range (k2, n):
        a[i1 + 1][i2] += a[i1][i2]//2
        a[i1][i2 + 1] += a[i1][i2]//2
sum1 = 0
for i2 in range (k2, n):
    sum1 += a[n][i2]
res1 = (sum1 * s) >> 100
print(str(res1)+ ' ' + str(s-res1))
