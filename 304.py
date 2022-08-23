def C(n, k):
    c = 1
    for i in range(k + 1, n + 1):
        c *= i
        c //= i - k
    return c
  
r = 1
l = input().split()
  
for s, f in zip(l[1:], [24] * 4 + [14]):
    a, b = map(int,s.split(':'))
    if a < b:
        a, b = b, a
          
    if a == f + 1:
        r *= C(a + b - 1,b)
    else:
        r *= C(2 * f, f) * (1 <<(b - f))
  
print(r)
