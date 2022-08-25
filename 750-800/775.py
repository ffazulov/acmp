n,m = map(str, input().split())
if m == '0':
    print('NO')
else:
    print(n[:-1]+str(int(n[-1])+1))
