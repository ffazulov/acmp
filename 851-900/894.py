n = [float(i) for i in input().split()]
import math
s = n[0]
a = n[1]
b = ((3.14159265359 * a ** 2 - s) / 3.14159265359) ** 0.5
b = int(b * 1000)
b = b / 1000
print(b)
