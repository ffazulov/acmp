my_list = [int(i) for i in input().split()]
my_list_ch = []
my_list_no_ch = []
for i in range(len(my_list)):
    if (i+1)%2==0:
        my_list_ch.append(my_list[i])
    else:
        my_list_no_ch.append(my_list[i])
print(max(my_list_ch) + min(my_list_no_ch))
