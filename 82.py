input()
a = set(map(int, input().split()))
b = set(map(int, input().split()))
if len(b) < len(a):
    a, b = b, a
c = []
for i in b:
    if i in a:
        c.append(i)
  
k = ' '.join(map(str, c))
print(k)
