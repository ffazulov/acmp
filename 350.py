import itertools
letters = input()
for s in itertools.permutations(letters):
    print(''.join(s))
