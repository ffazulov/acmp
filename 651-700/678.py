a = 1
b = 0
c = 0
infile = open('input.txt')
outfile = open('output.txt', 'w')
  
while True:
    s = infile.readline(1)
    if not s: break
    if s == 'A':
        a, b = b, a
    elif s == 'B':
        b, c = c, b
    elif s == 'C':
        a, c = c, a
  
if a == 1:
    outfile.write('1')
elif b == 1:
    outfile.write('2')
elif c == 1:
    outfile.write('3')
