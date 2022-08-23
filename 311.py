f = open('input.txt', 'r')
num = f.read()
f.close()
num = num.split()
  
print(num)
  
fact = 0
for i in range(1, int(num[0])+1):
    proiz = 1
    for j in range(1, i+1):
        proiz *=j
    fact +=proiz
  
o = open('output.txt', 'w')
o.write(str(fact))
o.close()
