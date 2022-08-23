k = int(input())
for i in range(k):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    while b > 0 and (a!=c or b!=d):
        if b == d and a >= c and (a-c) % b == 0:
            a = c
        else:
            a, b = b, a % b
    print(['NO','YES'][a == c and b == d])
