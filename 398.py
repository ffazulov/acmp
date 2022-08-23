k =0
n = int(input())
for a in range(1, (n//2)+1):
    for b in range(a, (n // 2) + 1):
        for c in range(b, (n // 2) + 1):
            d = n -(a+b+c)
            if d>= c:
                if a+b+c+d ==n:
                    k+=1
 
print(k)
