n = int(input())
l = []
for i in input().split():
    l.append(int(i))
k = 0
for i in range (n):
    if l[i] <= 437:
        print('Crash '+ str(i+1))
        k += 1
        break
if k == 0:
    print('No crash')
