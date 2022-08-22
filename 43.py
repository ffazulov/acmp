s = input()
b = 0
ab = 0
p = 0
i = 0
while i < len(s):
    if s[i] == '0':
        ab += 1
        if ab > p:
            p = ab
    if s[i] == '1':
        ab = 0
    i += 1
print(p)
