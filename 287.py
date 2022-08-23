def main():
    input_file = open("input.txt", "r")
    output_file = open("output.txt", "w")
    line = input_file.readline().split()
    n, m = int(line[0]), int(line[1])
    line = input_file.readline()
    s = list(line)
    if s[-1] == '\n':
        s.remove('\n')
    a = set()
    for i in range(n - m + 1):
        w = ""
        for j in range(m):
            w += s[i + j]
        a.add(w)
    print(a)
    print(s)
    ans = len(a)
    print(ans)
    output_file.write(str(ans) + '\n')
  
  
if __name__ == "__main__":
    main()
