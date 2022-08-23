n = int(input())
prev = float(input())
l, r = 30, 4000
  
for i in range(1, n):
    cur, s = input().split()
    cur = float(cur)
    if cur == prev:
        continue
    mid = (prev + cur) / 2
    if cur > prev and s == 'closer' or cur < prev and s != 'closer':
        l = max(l, mid)
    else:
        r = min(r, mid)
    prev = cur
print(l, r)
