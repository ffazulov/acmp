def main():
    input_file = open("INPUT.txt", "r")
    output_file = open("OUTPUT.txt", "w")
    line = input_file.readline().split()
    n = int(line[0])
    s = ""
    for i in range(n):
        line = input_file.readline().split()
        a, b, c = int(line[0]), int(line[1]), int(line[2])
        if c == 1 or c == 2 or (a % c == 0 and b % c == 2) or (b % c == 0 and a % c == 2) or (a % c == 1 and b % c == 1):
            s += "1"
        else:
            s += "0"
    print(s)
    output_file.write(str(s) + "\n")
    input_file.close()
    output_file.close()
main()
