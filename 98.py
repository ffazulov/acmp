n = int(input())
a = list(map (int, input().split()))
  
x = y = 0
for k in range(n):
    i = a[0]
    j = a[-1]
    if j > i:
        z = j
        del a[-1]
    else:
        z = i
        del a[0]
    if k & 1:
        y += z
    else:
        x += z
     
print(f'{x}:{y}')
