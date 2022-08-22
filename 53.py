n,m = map(int, input().split())
 
a = [[0 for i in range(m)] for i in range(n)]
 
for i in range(1, n+1):
    for j in range(1, m+1):
        if i*j%2==0:
            a[i-1][j-1]=1
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i * j % 3 == 0:
            a[i - 1][j - 1] = 2
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i * j % 5 == 0:
            a[i - 1][j - 1] = 3
 
s, s1, s2, s3 = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            s += 1
        if a[i][j]==2:
            s1+=1
        if a[i][j]==3:
            s2+=1
        if a[i][j]==0:
            s3+=1
 
print('RED : ',s)
print('GREEN : ',s1)
print('BLUE : ',s2)
print('BLACK : ',s3)
