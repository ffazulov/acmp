def AND(a, b):
    return a and b
  
def OR(a, b):
    return a or b
  
def NOT(a):
    return not a
  
  
s = input()
n,k = map(int,input().split())
  
FALSE, TRUE = False, True
for i in range (n):
    for j in range(k):
        exec(input())
    print(['FALSE', 'TRUE'][eval(s)])
