def steps(mm):
    for i, ch in enumerate(mm):
        if ch == 'B' or ch == 'W':
            for j in range(9):
                if mm[j] == '.' and (i // 3 - j // 3) ** 2 + (i % 3 - j % 3) ** 2 == 5:
                    res = [[mm[k], ch, '.'][(k == j) + 2 * (k == i)] for k in range(9)]
                    yield ''.join(res)
  
  
  
mm1, mm2 ='', ''
for i in range(3):
    l1, l2 = input().split()
    mm1 += l1
    mm2 += l2
      
q, ind = [mm1], 0
used = {mm1: 0}
while ind < len(q):
    mm = q[ind]
    ind += 1
    for nxt in steps(mm):
        if not nxt in used:
            q.append(nxt)
            used[nxt] = used[mm] + 1
print(used.get(mm2, -1))
