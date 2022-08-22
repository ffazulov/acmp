a,b = map(str, input().split())
def sB(a,b):
    check = 0
    for i in range(4):
        if a[i] == b[i]:
            check +=1
    return check
def sK(a,b):
    check = 0
    for i in range(4):
        for j in range(4):
            if a[i] == b[j] and i !=j:
                check +=1
    return check 
print(sB(a,b), sK(a,b))
