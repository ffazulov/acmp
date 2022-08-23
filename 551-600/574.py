with open("INPUT.TXT") as f:
    data = f.read().split()
dict_a = {}
dict_b = {}
for i in data[0]:
    dict_a[i] = dict_a.get(i, 0) + 1
for i in data[1]:
    dict_b[i] = dict_b.get(i, 0) + 1
with open("OUTPUT.TXT", "w") as f:
    if dict_a==dict_b:
        f.write("YES")
    else:
        f.write("NO")
