from math import trunc
  
_in = open('input.txt')
_out = open('output.txt', 'w')
  
k = int(_in.readline())
print(trunc((-1+(1+8*k)**0.5)/2), file=_out)
  
_in.close()
_out.close()
