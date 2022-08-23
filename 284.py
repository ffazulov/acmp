n=int(input())
m=[int(i) for i in input().split()]
kpm=int(input())
dm=[[int(j) for j in input().split()] for i in range (kpm)]
for i in range(kpm):
    for j in range (dm[i][0]-1,dm[i][1]):
        print(m[j],end=' ')
    print()
