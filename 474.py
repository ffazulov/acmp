n = int(input())
n -= 1
res = 0
while n > 0:
    if n % 3 == 2:
        res += 1
    n //= 3
print(res % 2)
