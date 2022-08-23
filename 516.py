import math
def pr(n):
    i = 2
    limit = int(math.sqrt(n))
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True
  
    print("It's prime number")
def main():
    input_file = open("input.txt", "r")
    output_file = open("output.txt", "w")
    line = input_file.readline().split()
    a = str(line[0])
    a = list(a)
    print(a)
    a.sort()
    s = ""
    for i in range(len(a)):
        s += a[i]
    a1 = int(s)
    s = ""
    a.reverse()
    for i in range(len(a)):
        s += a[i]
    a2 = int(s)
    
    if pr(a1) and pr(a2):
        ans = "Yes"
    else:
        ans = "No"
    print(ans)
    output_file.write(str(ans) + "\n")
  
    input_file.close()
    output_file.close()
  
  
if __name__ == "__main__":
    main()
