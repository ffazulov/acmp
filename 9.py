infile = open('INPUT.TXT')
ofile = open('OUTPUT.TXT', 'w')
  
infile.readline()
line = [int(x) for x in infile.readline().split()]
  
summ = 0
 
for x in line:
    if x>0:
        summ +=x
mul = 1
  
if line.index(min(line))>line.index(max(line)):
    for x in line[line.index(max(line))+1:line.index(min(line))]:
        mul *= x
else:
    for x in line[line.index(min(line))+1:line.index(max(line))]:
        mul *= x
  
print(summ, mul)
ofile.write(str(summ) + ' ' + str(mul))
  
infile.close()
ofile.close()
