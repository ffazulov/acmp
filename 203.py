a = list(input())
b = list(input())
cnt = 0
while a!=b:
  b+=b[0]
  b.pop(0)
  cnt+=1
  if cnt>len(a):
      break
print(cnt if cnt<=len(a) else -1)
