def check(x, arr):
  
    l, r = 0, len(arr) - 1
  
    while l <= r:
  
        m = (l + r) // 2
  
        if arr[m] > x:
  
            r = m - 1
  
        elif arr[m] < x:
  
            l = m + 1
  
        else:
  
            return True
  
    return False
  
 
  
 
  
def solve(n0):
  
    a = [1]
  
    while len(a) < n0:
  
        if check(len(a) + 1, a):
  
            a.append(a[-1] + 3)
  
        else:
  
            a.append(a[-1] + 2)
  
    print(a[-1])
  
 
  
 
  
n = int(input())
  
solve(n)
