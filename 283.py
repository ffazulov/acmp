import re
def check(s):
    words = re.findall(r'[A-Z][a-z]{1,3}', s)
    return ''.join(words) == s
  
f = check(input())
if f:
  print('Yes')
else:
  print('No')
