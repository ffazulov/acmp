with open('INPUT.TXT', 'r') as f:
    lst = [(ord(letter) - ord('A'), idx + 1) for idx, letter in enumerate(f.read(26))]
     
    lst.sort()
    flag = True
 
    for idx, item in enumerate(lst):
        if item[0] < idx:
            flag = False
            break
 
with open('OUTPUT.TXT', 'w') as f:
    if flag:
        f.write('YES\n')
        for item in lst:
            f.write(str(item[1]))
            f.write(' ')
    else:
        f.write('NO')
