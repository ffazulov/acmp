n = int(input())
a = n % 10
n //= 10
b = n % 10
n //= 10
c = n % 10
n //= 10
d = n % 10
if a == d and b == c:
    print("YES")
else:
    print("NO")
