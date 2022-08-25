girl = True
girl2 = False
boy = False
m, n = map(int, input().split())
while n or m:
    if girl:
        if n:
            print('G', end='')
            n-=1
        girl = False
        girl2 = True
    if girl2:
        if n:
            print('G', end='')
            n-=1
        girl2 = False
        boy = True
    if boy:
        if m:
            print('B', end='')
            m-=1
        girl = True
        boy = False
