n, m = map(int, input().split())
 
a = []
c = []
s = 0
 
for i in range(n):
    b = input()
    a.append(list(b))
input()
for i in range(n):
    b = input()
    c.append(list(b))
 
for i in range(n):
    for j in range(m):
        if a[i][j] == c[i][j]:
            s += 1
 
print(s)
