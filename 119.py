x = int(input())
l = []
for i in range(x):
    a = [int(i) for i in input().split()]
    l.append(a)
def search_min(l):
    t = l[0][0]*3600 + l[0][1]*60 + l[0][2]
    k = 0
    for i in range(1, len(l)):
        if (l[i][0]*3600 + l[i][1]*60 + l[i][2]) < t:
            t = l[i][0]*3600 + l[i][1]*60 + l[i][2]
            k = i
    return k
for i in range(x):
    k = search_min(l)
    print(l[k][0], l[k][1], l[k][2])
    l.pop(k)
