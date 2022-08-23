n = int(input())
c = [0 for i in range(31)]
for i in range(n):
    a, b = map(int, input().split())
    for j in range(a, b+1):
        c[j-1]+=1
for i in range(31):
    if c[i]==n:
        print('YES')
        exit()
print('NO')
