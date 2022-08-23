n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
perem = int(0)
result = 0
maxPerem = -1
for i in range(n):
    perem = a[i]*b[i]
    if perem > maxPerem:
        maxPerem = perem
        result = i+1
print(result)
