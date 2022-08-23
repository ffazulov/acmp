n, m, k = map(int, input().split())
k += 1
left, right, bottom, top = [201]*k, [-1]*k, [201]*k, [-1]*k
  
def update(ind):
    left[ind] = min(left[ind], x)
    right[ind] = max(right[ind], x)
    bottom[ind] = min(bottom[ind], y)
    top[ind] = max(top[ind], y)
  
for y in range(n-1, -1, -1):
    line = map(int, input().split())
    for x, a in enumerate(line):
        if a == 0:
            continue
        update(a)
        update(0)
  
for i in range(1, k):
    if left[i] < 201:
        print(left[i], bottom[i], right[i] + 1, top[i] + 1)
    else:
        print(left[0], bottom[0], right[0] + 1, top[0] + 1)
