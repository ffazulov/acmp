n = [int(i) for i in input().split()]
 
mid_cost = [n[0], n[1], n[2]]
mid_count = [n[3], n[4], n[5]]
money1 = 0
for i in range(3):
    max_cost = max(mid_cost)
    max_count = max(mid_count)
    money = max_count * max_cost
    money1 += money
    mid_cost.remove(max_cost)
    mid_count.remove(max_count)
 
print(money1)
