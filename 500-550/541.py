s = input()
t = input()
  
mx, mn = 0 , 10 ** len(t)
for i in range(len(s)):
    mx = max(mx, int(s[i:] + s[:i]))
  
for i in range(len(t)):
    if t[i] != '0':
        mn = min(mn, int(t[i:] + t[:i]))
  
print(mx - mn)
