screw = [int(i) for i in input().split()]
bolt = [int(i) for i in input().split()]
 
res1 = screw[0]//100*screw[1]*screw[2]#-------
 
res2 = bolt[0]//100*bolt[1]*bolt[2]#---------
 
 
count_screw = (screw[0]-(screw[0]//100*screw[1]))
count_bolt = (bolt[0]-(bolt[0]//100*bolt[1]))
if count_bolt == max(count_screw, count_bolt):
    res3 = (count_bolt-count_screw)*bolt[2]
else:
    res3 = (count_screw-count_bolt) * screw[2]
print(round(res2+res1+res3))
