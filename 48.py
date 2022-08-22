f = open('INPUT.TXT')
c = f.read()
f.close()
c = c.strip()
c = int(c)
r = '1'
q = 0
while c%10 == 0:
    r+= '0'
    c = c//10
  
f = open('OUTPUT.TXT', 'w')
f.write(str(r))
f.close()
