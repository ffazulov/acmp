import math
a, b, c = map(int,input().split())
l =[]
l.append(b)
l.append(c)
d = math.fabs(b-c)
e = math.fabs((a-max(l))+min(l))
if d > e:
    print(int(e)-1)
else:
    print(int(d)-1)
