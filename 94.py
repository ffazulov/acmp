n,m,k = map(int, input().split())
if n>=m:
    print(1)
else:
    if n<=k:
        print('NO')
    else:
        print((m-n-1)//(n-k)+2)
