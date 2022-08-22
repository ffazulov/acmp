k, n = map(int, input().split())
a = input()
  
d = [a[x:x+n] for x in range(len(a) - n + 1)]
r = list(set(d))
if len(r) != len(d):
    print('YES')
else:
    print('NO')
