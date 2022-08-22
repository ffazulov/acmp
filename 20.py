n = int(input())
lst = list(map(int, input().split()))
result = 2 if n > 1 and lst[0] != lst[1] else 1
current = result
for i in range(2, n):
    if lst[i] > lst[i - 1] < lst[i - 2] or lst[i] < lst[i - 1] > lst[i - 2]:
        current += 1
    else:
        current = 2 if lst[i] != lst[i - 1] else 1
    result = max(result, current)
print(result)
