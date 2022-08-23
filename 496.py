input()
lst = [int(i) for i in input().split()]
 
new_lst = [lst[0]+lst[-1]+lst[-2], lst[0]+lst[1]+lst[-1]]
for i in range(len(lst)-2):
    r = lst[i]+lst[i+1]+lst[i+2]
    new_lst.append(r)
print(max(new_lst))
