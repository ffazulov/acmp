import re
x = input()
teg = r'[0]*[1]'
c = ''
for i in re.findall(teg, x):
    c += chr(len(i)+96)
print(c)
