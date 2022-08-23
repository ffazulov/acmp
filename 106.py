n = int(input())
list1 = []
for i in range(n):
  x = int(input())
  list1.append(x)
count = 0
for i in list1:
  count = i + count
result_1 = count
result_0 = n - result_1
if result_0 > result_1:
  print(result_1)
if result_0 < result_1:
  print(result_0)
if result_0 == result_1:
  print(result_1)
