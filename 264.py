x = int(input())
my_list = [int(i) for i in input().split()]
max_long = 0
positiv = 0
longers = []
for i in my_list:
    if i > 0:
        positiv += 1
        longers.append(positiv)
    else:
        longers.append(positiv)
        positiv = 0
print(max(longers))
