maxJump, n = map(int, input().split())
count = [1,1] + [0] * (2+n-2)
for i in range(2, maxJump + 1):
    count[i] = count[i-1] << 1
for i in range(maxJump+1, n+1):
    count[i] = (count[i-1] << 1) - count[i-1-maxJump]
print(count[n])
