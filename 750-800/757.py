with open("INPUT.TXT", "r") as f:
    c, h, o = map(int, f.readline().split(" "))
    with open("OUTPUT.TXT", "w") as f1:
        f1.write(str(min(c // 2, h // 6, o)))
