def factorial(n):
    k = 0
    p = 1
    for i in range(n):
        k += 1
        p *= k
    return p
n = int(input())
g = factorial(n)
rem = g%10
while rem == 0:
    g//= 10
    rem = g%10
print(rem)
