n = int(input())
k = 1
s = 0
 
if n>145:
    print('NO')
    exit()
while k<n:
    s+=5
    k+=1
print(s//60, ' ', s%60)
