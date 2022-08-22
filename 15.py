x = int(input())
M = []
for i in range (x):
    M.append([])
    M[i] = [int(j) for j in input().split()]
      
res = 0
for i in range (x):
    for j in range (x):
        if M[i][j] == 1:
            res +=1
  
print(int(res//2))
