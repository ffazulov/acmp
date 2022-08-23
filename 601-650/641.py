s = input()
lenght = len(s)
for i in range(lenght-1):
    if s[i]<s[i+1]:
        s = s[:i] + s[i + 1:]
        break
else:
    print(s[:-2])
    exit()
for i in range(lenght-2):
    if s[i]<s[i+1]:
        s=s[:i]+s[i+1:]
        break
else:
    print(s[:-1])
    exit()
print(s)
