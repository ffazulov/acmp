a = []
s = 0
 
for i in range(4):
    b = input()
    a.append(list(b))
 
for i in range(3):
    for j in range(3):
        if (a[i][j] == a[i][j+1] == 'W' and a[i+1][j] == a[i+1][j+1] == 'W') or (a[i][j] == a[i][j+1] == 'B' and a[i+1][j] == a[i+1][j+1] == 'B'):
            print('No')
            break
        else:
            s += 1
if s == 9:
    print('Yes')
