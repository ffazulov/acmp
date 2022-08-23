b = 0
a = int(input())
while a:
  b = b*2+a%2
  a= a//2
print(b)
