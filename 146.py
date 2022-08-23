n = int(input())
a = n+1
next = n
while next < a:
    a = next
    next = (a+n//a)//2
print(a)
