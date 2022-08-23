n, m = map(int, input().split())
rm, rs ="", m * 9999
for i in range(n):
    name = input()
    sm = sum(map(int, input().split()))
    if sm < rs:
        rm, rs = name, sm
print(rm)
