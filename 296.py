count5 = count3 = s = 0
k = int(input())
if k==6 or k==3 or k==9 or k==12:
    print(0,' ',k//3)
    exit()
while s<k:
    s+=5
    count5+=1
    if (k - (count5 * 5)) % 3==0 and (k - (count5 * 5)) % 5!=0 and (k - (count5 * 5) < 20):
        count3 = (k-(count5*5))//3
        s+=count3*3
print(count5,' ',count3)
