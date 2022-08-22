def mult(ax,ay,bx,by):  
    return ax * by - ay * bx
  
def get_square(ax,ay,bx,by,cx,cy):
    return abs(mult(ax-bx,ay-by,cx-bx,cy-by))
  
n = int(input())
result = 0
  
for i in range (n):
    lst = list(map(int, input().split()))
    x, y = lst[0], lst[1]
    xs = lst[2::2]
    ys = lst[3::2]
    s = 0
    for i in range(4):
        s += get_square(xs[i-1],ys[i-1],xs[i],ys[i],x,y)
    if s== 2 * get_square(xs[1],ys[1],xs[2],ys[2],xs[3],ys[3]):
        result += 1
print(result)
