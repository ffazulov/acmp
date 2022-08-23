a, b, c = map(int,input().split())
s = ''
if a ==0 and b ==0 and c == 0:
    print(0)
else:
    if a !=0:
        s += str(a)
    if b != 0:
        if b <0:
            if b != -1:
                s += str(b)
            else:
                s += '-'
            s += 'x'
        else:
            if a != 0:
                s += '+'
            if b != 1:
                s += str(b)
            s += 'x'
    if c!= 0:
        if c< 0:
            if c != -1:
                s += str(c)
            else:
                s += '-'
            s += 'y'
        else:
            if (b != 0) or (a!=0):
                s += '+'
            if c != 1:
                s += str(c)
            s += 'y'
print(s)
