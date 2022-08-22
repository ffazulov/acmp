a, b = map(int, input().split())
c = a * b
while a!=b:
    if a > b:
        a = a - b
    if b > a:
        b = b - a
print(c//a)
