from math import factorial
  
n,k = map(int,input().split())
if k > n :
    print(0)
else:
    print(factorial(n)**2 // factorial(n-k)**2 // factorial(k))
