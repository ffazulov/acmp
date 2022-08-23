a, b = map(int, input().split())
m = 100
for i in range(a):
    string=input()
    c = 0
    for el in string:
        if el == '.':
            c+=1
    if m > c:
        m = c
print(m)
