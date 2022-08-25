with open("INPUT.TXT", "r") as f:
    n = int(f.readline())
    x = list(map(int, f.readline().split()))
    with open("OUTPUT.TXT", "w") as q:
        q.write(str(sum(x) - n + 1))
