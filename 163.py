c1, s, c2, _, c3 = input()
if c1 == "x":
    print(int(c3) - int(s + c2))
elif c2 == "x":
    print((int(c3) - int(c1)) * (1 if s == "+" else -1))
else:
    print(int(c1) + int(s + c2))
