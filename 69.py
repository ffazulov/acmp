import math
def main():
    input_file = open("input.txt", "r")
    output_file = open("output.txt", "w")
    line = input_file.readline().split()
    n, a = int(line[0]), int(line[1])
    R = a / (2 * math.sin(math.pi / n))
    r = R * math.cos(math.pi / n)
    k = R - r
    if k < 1:
        ans = "YES"
    else:
        ans = "NO"
    output_file.write(str(ans) + "\n")
  
  
  
if __name__ == "__main__":
    main()
