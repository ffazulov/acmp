a = int(input())
res = 1
while (a > 1):
    if (a - 3 > 4):
        res = res * 3
        a = a - 3
    elif (a == 7):
        res = res * 4 * 3
        a = a - 7
    elif (a == 6):
        res = res * 3 * 3
        a = a - 6
    elif (a == 5):
        res = res * 2 * 3
        a = a - 5
    elif (a == 4):
        res = res * 4
        a = a - 4
    elif (a == 3):
        res = res * 3
        a = a - 3
    elif (a == 2):
        res = res * 2
        a = a - 2
    else:
        break
print(res)
