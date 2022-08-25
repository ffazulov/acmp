A,B,C,T = map(int, input().split())
if T > A:
    print((T-A)*C+(A*B))
else:
    print(T*B)
