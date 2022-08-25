f = [i for i in input().split()]
# word = list('QWERTY')
k = int(f[0]) - 1
word = list(f[1])
del word[k]
print(''.join(word))
