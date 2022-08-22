n = int(input())
lst = list(input(). split())
for i in range(1, n):
    if (n - 1) % i == 0 and lst[:-i] == lst[i:]:
        print(i)
        break
