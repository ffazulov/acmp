import math
def cnk(n, k):
    return math.factorial(n) / ((math.factorial(k)) * math.factorial(n - k))
def main():
    input_file = open("input.txt", "r")
    output_file = open("output.txt", "w")
    line = input_file.readline().split()
    n, m = int(line[0]), int(line[1])
    ans = 0
    for i in range(m, n + 1):
        ans = ans + cnk(n, i)
    print(ans)
    ans = int(ans)
    output_file.write(str(ans) + "\n")
    input_file.close()
    output_file.close()
main()
