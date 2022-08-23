n = int(input())
  
f0 = 1
f1 = 1
for i in range((n-1)%60):
    c= f1
    f1 = f1 + f0
    f0 = c
print(str(f1)[-1])
