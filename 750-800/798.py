m,n,i,j,c = map(int, input().split())
 
if (m%2==0) or (n%2==0):
    print('equal')
    exit()
     
if c==0:
    if (i+j)%2:
        print('white')
    else:
        print('black')
else:
    if not (i+j)%2:
        print('white')
    else:
        print('black')
