a = input()
for i in range(len(a) - 1):
    b = sum([int(i) for i in a[:i + 1]])
    c = sum([int(i) for i in a[i + 1:]])
    while b > 9:
        b = sum([int(i) for i in str(b)])
    while c > 9:
        c = sum([int(i) for i in str(c)])
    if b == c:
        print('YES')
        break
else:
    print('NO')
