a = str(input())
b = input().split()
hour = (int(a[0])*10 + int(a[1]) + int(b[0]) + ((int(a[3])*10+int(a[4])+int(b[1]))//60))%24
minute = ((int(a[3])*10+int(a[4])) + int(b[1]))%60
if hour <= 9:
    hour = str('0'+str(hour))
if hour == 0:
    hour = str('00')
if minute == 0:
    minute = str('00')
elif minute <= 9:
    minute = str('0'+str(minute))
print(str(hour)+':'+str(minute))
