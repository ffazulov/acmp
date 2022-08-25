n, m = map(int, input().split())
if n == 0 and m == 0:
    res = str(n)+' '+str(m)
elif n == 0 and m != n:
    res = 'Impossible'
elif m == 0:
    res = str(n)+' '+str(n)
elif n ==1:
    res = str(m)+' '+str(m)
elif n<m:
    res = str(m)+' '+str(m+n-1)
elif n==m:
    res = str(n)+' '+str(m+n-1)
else:
    res = str(n)+' '+str(m+n-1)
print(res)
