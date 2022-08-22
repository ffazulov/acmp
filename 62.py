x = list(input())
x[1] = int(x[1])
x[0] = int(ord(x[0]))
if x[0]%2==0 and x[1]%2!=0:
    print('WHITE')
elif x[0]%2==0 and x[1]%2==0:
    print('BLACK')
elif x[0]%2!=0 and x[1]%2!=0:
    print('BLACK')
elif x[0]%2!=0 and x[1]%2==0:
    print('WHITE')
