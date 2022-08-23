def matches(squares):
    side = int(squares**0.5)
    delta = squares - side**2
    count = 2 * side * (side + 1)
    if delta > 0:
        count += 3 + 2 * (delta - 1) + (1 if delta > side else 0)
    return count
print(matches(int(input())))
