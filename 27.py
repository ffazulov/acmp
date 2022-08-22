w, h = map(int, input().split())
  
forma = w * h
res = []
for i in range(w):
    res.append([0] * h)
  
  
def zap(s):
    *mass, = map(int, s.split())
    for i in range(mass[0], mass[2]):
        res[i][mass[1]:mass[3]] = [1] * (mass[3] - mass[1])
  
  
for k in range(int(input())):
    zap(input())
  
for i in range(len(res)):
    forma -= res[i].count(1)
print(forma)
