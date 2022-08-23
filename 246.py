def main():
    input_file = open("input.txt", "r")
    output_file = open("output.txt", "w")
    line = input_file.readline().split()
    n = int(line[0])
    arr = []
    line = input_file.readline().split()
    for i in range(n):
        arr.append(int(line[i]))
    print(arr)
    count = 0
    for i in range(n - 1):
        if arr[i] - arr[i + 1] != -1:
            count += 1
    print(count)
    output_file.write(str(count) + "\n")
    input_file.close()
    output_file.close()
  
  
if __name__ == "__main__":
    main()
