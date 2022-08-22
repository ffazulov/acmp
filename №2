file = open('INPUT.TXT', 'r')
N = file.read()
file.close()
N = N.split()
  
numb = ''
for i in N:
    numb += i
  
n = int(numb)
print(n)
  
summ = 0
if n > 0:
    for i in range (1, n+1):
        summ +=i
elif n < 0:
    for j in range (1, n-1, -1):
        summ +=j
else:
    summ = 1  
  
file2 = open('OUTPUT.TXT', 'w')
file2.write(str(summ))
file2.close()
