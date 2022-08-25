def check_len(word1, word2):
    word1_len = len(word1)
    word2_len = len(word2)
    if word1_len == word2_len:
        return True
    else:
        return False
 
def check_symbols(word1, word2):
    for s in list(word1):
        if s not in list(word2):
            return False
    for s in list(word2):
        if s not in list(word1):
            return False
    return True
 
def check_index(word1, word2):
    lst_word1 = list(word1)
    lst_word2 = list(word2)
    for i in range(len(lst_word1)):
        if lst_word1[i] == lst_word2[i]:
            return False
    return True
 
word = [i for i in input().split()]
 
if check_len(word[0], word[1]) and check_symbols(word[0],word[1]) and check_index(word[0],word[1]):
    print('YES')
else:
    print('NO')
