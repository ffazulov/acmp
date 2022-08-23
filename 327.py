x = int(input())
m = []
res = 0
for i in range(x):
    m.append(input())
def check(c):
    if ((int(c[0])+int(c[1])+int(c[2])) - (int(c[3])+int(c[4])+int(c[5])) == 1 and c[5] == '9') or ((int(c[0])+int(c[1])+int(c[2])) - (int(c[3])+int(c[4])+int(c[5])) == -1 and c[5] == '0'):
        print('No')
    else:
        print('Yes')
for i in range(x):
    check(m[i])
