n = int(input())
pos = (n*n+1)//2
ans = (pos - 1)//9*10+(pos-1)%9 +1
print(ans)
