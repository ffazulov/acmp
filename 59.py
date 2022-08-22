a,b = map(int,input().split())
def per(a,b):
    res = a%b
    a = a//b
    mn = 10
    while a>0:
        res = res+((a%b)*mn)
        mn *= 10
        a = a//b
    return res
  
def otvet(a):
    s = 0
    p = 1
    while a>0:
        x = a%10
        a = a//10
        s +=x
        p *=x
    return p-s
print(otvet(per(a,b)))
