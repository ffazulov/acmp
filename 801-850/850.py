a  =[int(i) for i in input().split()]
if a[0] < a[1]:
  a[0], a[1] = a[1], a[0]
print((a[0] + 1) // 2, a[1])
