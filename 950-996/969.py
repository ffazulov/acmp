n, m = map(int, input().split())
res = 2% m 
for i in range(1, n+1):
    res = (res*res)%m
print(res)
