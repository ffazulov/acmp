with open("INPUT.TXT", "r") as f:
    k, n = map(int, f.readline().split())
    with open("OUTPUT.TXT", "w") as q:
        q.write(f"{n // k + int(not(n % k == 0))} {n % k if n % k != 0 else k}")
