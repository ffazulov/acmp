n = input()
 
s = 0
 
for digit in n:
 
   if digit in ['0', '6', '9']:
 
       s += 1
 
   elif digit == '8':
 
       s += 2
 
print(s)
