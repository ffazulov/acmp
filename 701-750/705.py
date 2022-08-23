def fast_pow(a, b, mod):
    res = 1 % mod
    while b > 0:
        if b % 2 == 1:
            res = (res*a)% mod
        a = (a*a)% mod 
        b //= 2
    return res
  
n, m = map(int, input().split())
print((fast_pow(2, n, m)*(n*n-4*n+6)-6)% m)
