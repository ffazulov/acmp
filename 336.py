x = input()
maxE = 0
minE = 0
T = 0
for i in range(len(x)):
    if x[i] =='1':
        T += 1
    else:
        T -= 1
    if maxE < T:
        maxE = T
    elif minE > T:
        minE = T
print(abs(minE)+abs(maxE)+1)
