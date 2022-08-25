from math import pi
my_list = [int(i) for i in input().split()]
s2 = my_list[2] * 2
if my_list[0] >= s2 and my_list[1] >= s2:
    print('YES')
else:
    print('NO')
