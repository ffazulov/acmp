n1 = int(input())
s = ''.join([str(i) for i in range(1, n1+1)])
print(str(s).find(str(n1)) + 1)
