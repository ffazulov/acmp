n, a, b = map(int, input().split())
for i in range(n , 1 , -1):
    c = b - a
    b = a
    a = c
print(a, b, end=' ')
