age, sm = input(). split()
age = int(age[-1]) + 2
  
result, p = 0, 1
mp = {str(a): a for a in range(10)}
mp['A'] = 10
mp['B'] = 11
for digit in sm[::-1]:
    result += p * mp[digit]
    p *= age
      
print(result)
