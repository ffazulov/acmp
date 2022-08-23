n, k = map(int, input().split())
result = 1+(n-1)*k
for i in range(k):
  result += i*(n-2)
print(result)
