n = int(input())
a = [0 for i in range(100)]
b = [0 for i in range(100)]
bb = [int(i) for i in input().split()]
for el in bb:
  a[el-1]+=1
  b[el-1]+=1
b = sorted(b)
if b[len(b)-1] == b[len(b)-2]:
  print(0)
  exit()
for i in range(len(a)):
  if a[i] == b[len(b)-1]:
    print(i+1)
    exit()
