w,h = map(int, input().split())
m1 = [input() for i in range(h)]
m2 = [input() for i in range(h)]
  
d = {}
d['00'], d['01'], d['10'], d['11'] = input()
  
for l1, l2 in zip(m1, m2):
    for c1, c2 in zip (l1,l2):
        print(d[c1+c2], end='')
    print()
