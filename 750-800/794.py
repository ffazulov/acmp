def main():
    input_file = open("input.txt", "r")
    output_file = open("output.txt", "w")
    line = input_file.readline().split(' ')
    n, m, k = int(line[0]), int(line[1]), int(line[2])
    if m < k:
        ans = n * m
    else:
        ans = ((k - 1) + int(m / k)) * n
    output_file.write(str(ans) + "\n")
  
if __name__ == "__main__":
    main()
