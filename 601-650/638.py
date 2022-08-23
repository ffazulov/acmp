n, k = map(int, input().split())
w, dw, s = map(int, input().split())
dp = [0] * n
for h in map(int, input().split()):
    for i in range((h - s + w) % w, n, w):
        dp[i] = -1
if int(input()) > 0:
    for h in map(int, input().split()):
        dp[h - 1] = -1
dp[0] += 1
for i in range(1, n):
    dp[i] = dp[i - 1] + 1 if dp[i] == 0 else 0
print(len(list(filter(lambda e: e>=k,dp))))
