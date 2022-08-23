for _ in range(int(input())) : print((lambda A, B : ("NO","YES")[set(list(A)) == set(list(B))])(*(input().split())))
