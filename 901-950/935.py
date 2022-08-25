k, l, m, n = map(int,input().split())
print(["YES", "NO"][sum([k, l, m, n]) & 1])
