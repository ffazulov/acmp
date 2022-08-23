x = str(input())
if len(x)<4:
    for i in range(4-len(x)):
        x = '0'+x
if (int(x)%400==0) or (int(x)%4==0)and(int(x)%100 != 0):
    print('12/09/' + x)
else:
    print('13/09/' + x)
