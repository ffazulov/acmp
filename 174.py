input()
z = sorted(map(int, input().split()))
p = int(input())
for i in z:
    if i > p:
        p = (p + i) / 2
print(f'{p:.6f}')
