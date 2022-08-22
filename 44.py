i = list(input())
count = 0
for el in range(len(i)-4):
    if i[el] == '<':
        if i[el+1] == '-':
            if i[el+2] == '-':
                if i[el+3] == '<':
                    if i[el+4] == '<':
                        count +=1
    if i[el] == '>':
        if i[el+1] == '>':
            if i[el+2] == '-':
                if i[el+3] == '-':
                    if i[el+4] == '>':
                        count +=1
print(count)
