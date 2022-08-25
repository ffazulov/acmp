n = int(input())
a = b = c = n // 3
d = a//2 + c//2
b += d
a = c = a//2
  
d = a//2 + b//2
c += d
a //= 2
b //= 2
  
d = b//2 + c//2
a += d
b //= 2
c //= 2
  
print(a,b,c)
