def AND(*args):
    res = True
    for arg in args:
        res = res and arg
    return res
  
def OR(*args):
    res = False
    for arg in args:
        res = res or arg
    return res
  
def NOT(a):
    return not a
  
  
s = input()
n,k = map(int,input().split())
  
FALSE, TRUE = False, True
for i in range (n):
    for j in range(k):
        exec(input())
    print(['FALSE', 'TRUE'][eval(s)])
