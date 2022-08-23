n,v,k = map(int, input().split())
total = v
isEmpty = False
i = 1
while i<n and not isEmpty:
    currentDonation = v-k*i
    if currentDonation>0:
        total += currentDonation
    else:
        isEmpty = True
    i+=1
if not isEmpty:
    isEmpty = 'YES'
else:
    isEmpty = "NO"
print(isEmpty, ' ', total)
