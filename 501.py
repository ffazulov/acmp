def get_len(a, b, c, d):
    return max(0, min(b, d) - max(a, c))
             
def get_square(i, j):
    x = get_len(x1[i], x2[i], x1[j], x2[j])
    y = get_len(y1[i], y2[i], y1[j], y2[j])
    return x * y
  
n = int(input())
n += 1
x1, y1, x2, y2 = [0] * n, [0] * n, [0] * n, [0] * n
for i in range(n):
    x1[i], y1[i], x2[i], y2[i] = map(int, input().split())
    if x1[i] > x2[i]:
        x1[i], x2[i] = x2[i], x1[i]
    if y1[i] > y2[i]:
        y1[i], y2[i] = y2[i], y1[i]
res = 0
for i in range(n - 1):
    res += get_square(i, -1)
print(res)
