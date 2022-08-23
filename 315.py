a = str(input())
maxOrd = -1
for i in range(len(a)):
    if (ord(a[i]) > 64 and ord(a[i]) < 91) or (ord(a[i]) < 58 and ord(a[i]) > 47):
        if ord(a[i]) > maxOrd:
            maxOrd = ord(a[i])
    else:
        maxOrd = -1
        break
if int(maxOrd) == 48:
    print(2)
elif int(maxOrd) > 60:
    print(int(maxOrd) - 54)
elif int(maxOrd) != -1:
    print(int(maxOrd) - 47)
else:
    print(int(maxOrd))
