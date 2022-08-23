k, w = map(int, input().split())
a1, b1, a2, b2, a3, b3 = map(int, input().split())
a = [a1, a2, a3, a1 + a2, a1 + a3, a2 + a3, a1 + a2 + a3]
b = [b1, b2, b3, b1 + b2, b1 + b3, b2 + b3, b1 + b2 + b3]
r = False
for i in range(7):
  if b[i] >= k and a[i] <= w:
    r = True
    break
print('YES' if r else 'NO')
