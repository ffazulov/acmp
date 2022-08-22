user = input()
my_list = user.split()
x1 = int(my_list[0])
x2 = int(my_list[1])
x3 = int(my_list[2])
if x1 <= x2 and x2 >= x3:
  maxim = x2
if x2 <= x1 and x1 >= x3:
  maxim = x1
if x1 <= x3 and x3 >= x2:
  maxim = x3
 
if x1 <= x2 and x3 >= x1:
  minim = x1
if x2 <= x1 and x3 >= x2:
  minim = x2
if x3 <= x1 and x2 >= x3:
  minim = x3
result = maxim - minim
print(result)
