x = int(input())
a = 2
while (a<10000):
    if a == x or x == 1:
        print('YES')
        break
    a = a*2
if a != x and x != 1:
    print('NO')
