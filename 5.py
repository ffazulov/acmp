all_count = input()
counts = [int(i) for i in input().split()]
ch = []
nech = []
for i in counts:
    if i % 2 == 0:
        ch.append(i)
    else:
        nech.append(i)
print(*nech)
print(*ch)
if len(ch)>=len(nech):
    print('YES')
else:
    print('NO')
