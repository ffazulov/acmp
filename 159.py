def main():
    input_file = open("input.txt", "r")
    output_file = open("output.txt", "w")
    line = input_file.readline().split()
    n = int(line[0])
    line = input_file.readline().split()
    a = []
    b = []
    for i in range(1, n + 1):
        a.append((i, int(line[i - 1])))
        b.append(0)
    for i in range(len(a)):
        b[a[i][1] - 1] = a[i][0]
    print(b)
  
  
  
    output_file.write(str(' '.join(str(x) for x in b)) + '\n')
  
    input_file.close()
    output_file.close()
  
  
if __name__ == "__main__":
    main()
