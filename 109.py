f = open('INPUT.TXT')
c = f.read()
f.close()
c = c.split('/')
c[0],c[1] = int(c[0]), int(c[1])
  
def convert(numerator, denominator):
    ans = str(numerator//denominator)+'.'
    l = {}
    index = 0
    numerator = numerator%denominator
    l[numerator] = index
    t=False
    while t==False:
        if numerator==0:
            break
        digit = numerator*10//denominator
        numerator=numerator*10-(numerator*10//denominator)*denominator
        if numerator not in l:
            ans+=str(digit)
            index +=1
            l[numerator]=index
            t=False
        else:
            ans+=str(digit)+')'
            ans = ans[:l.get(numerator)+len(ans[:ans.index('.')+1])]+'('+ ans[l.get(numerator)+len(ans[:ans.index('.')+1]):]
            t=True
    return ans
r= convert(c[0],c[1])
e = r.split('.')
if e[1]=='':
    r = e[0]
f = open('OUTPUT.TXT', 'w')
f.write(str(r))
f.close()
