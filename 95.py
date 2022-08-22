# -*- coding: utf-8 -*-
tm = input()
N = int(tm)
res = N
res1 = 0
while res > 9:
    a = res
    res = 0
    res1 = res1 + 1
    for i in range(len(str(a))):
        res = res + a%10
        a = a//10
print(str(res)+' '+str(res1))
