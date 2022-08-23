A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))
A = sorted(A)
B = sorted(B)
if A[0] > B[0]:
    if A[1] >= B[1]:
        if A[2] >= B[2]:
            print('The first box is larger than the second one')
        else:
            print('Boxes are incomparable')
    else:
        print('Boxes are incomparable')
else:
    if A[0] < B[0]:
        if A[1] < B[1]:
            if A[2] < B[2]:
                print('The first box is smaller than the second one')
            else:
                print('Boxes are incomparable')
        else:
            print('Boxes are incomparable')
    else:
        if A[1] > B[1]:
            if A[2] >= B[2]:
                print('The first box is larger than the second one')
            else:
                print('Boxes are incomparable')
        else:
            if A[1] < B[1]:
                if A[2] <= B[2]:
                    print('The first box is smaller than the second one')
                else:
                    print('Boxes are incomparable')
            else:
                if A[2] > B[2]:
                    print('The first box is larger than the second one')
                else:
                    if A[2] < B[2]:
                        print('The first box is smaller than the second one')
                    else:
                        print('Boxes are equal')
