s = 0
n = int(input())
for i in range(1, n+1):
    s+=i
    if s==n:
        print(i)
        exit()
print(s)
