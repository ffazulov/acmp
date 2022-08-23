def main():
    input_file = open("input.txt", "r")
    output_file = open("output.txt", "w")
    line = input_file.readline().split()
    n = str(line[0])
    print(n)
    a = []
    for i in range(101):
        b = []
        for j in range(101):
            b.append(0)
        a.append(b)
    print(a)
    i = 5
    j = 5
    a[i][j] = 1
    flag = [1, 2, 3, 4]
    f = 1
    count = 0
    fff = False
    for k in range(len(n)):
        if n[k] == "S" and f == 1:
            count += 1
            if a[i - 1][j] == 1:
                fff = True
                break
            a[i - 1][j] = 1
            i = i - 1
  
        if n[k] == "S" and f == 2:
            count += 1
            if a[i][j + 1] == 1:
                fff = True
                break
            a[i][j + 1] = 1
            j = j + 1
        if n[k] == "S" and f == 3:
            count += 1
            if a[i + 1][j] == 1:
                fff = True
                break
            a[i + 1][j] = 1
            i = i + 1
        if n[k] == "S" and f == 4:
            count += 1
            if a[i][j - 1] == 1:
                fff = True
                break
            a[i][j - 1] = 1
            j = j - 1
        if n[k] == "R":
            f = (f + 1) % 4
            if f == 0:
                f = 4
        if n[k] == "L":
            f = abs(f - 1) % 4
            if f == 0:
                f = 4
  
    for i in range(101):
        print(a[i])
    print(count)
    if fff == True:
        ans = count
    else:
        ans = -1
  
    print(ans)
  
  
    output_file.write(str(ans) + "\n")
    input_file.close()
    output_file.close()
  
  
if __name__ == "__main__":
    main()
