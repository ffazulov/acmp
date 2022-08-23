def mult(x0, y0, x1, y1):
    return x0 * y1 - x1 * y0
def scal(x0, y0, x1, y1):
    return x0 * x1 + y0 * y1
def sign(a):
    return (a > 0) - (a < 0)
  
sz = int(input())
n = int(input())
lst = list(map(int, input().split()))
  
flag = False
x0, y0 = sz / 2, sz / 2
for i in range(n):
    x1, y1 = lst[2 * i: 2 * i + 2]
    c = [0, 0, 0]
    c0 = [0, 0, 0]
    for j in range(n):
        x2, y2 = lst[2 * j: 2 * j + 2]
        vect = mult(x1 - x0, y1 - y0, x2 - x0, y2 - y0)
        c[sign(vect)] += 1
        if vect == 0:
            sc = scal(x1 - x0, y1 - y0, x2 - x0, y2 - y0)
            c0[sign(sc)] += 1
    flag |= (c[-1] + c0[1] == n) or (c[1] + c0[1] == n)
print(["NO", "YES"][flag])
