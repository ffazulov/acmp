def main():
    input_file = open("input.txt", "r")
    output_file = open("output.txt", "w")
    line = input_file.readline().split()
    a = set(line[0])
    b = str(line[0])
    c = int(line[0])
    size = len(b)
    print(size)
    print(a)
    if len(a) <= 2:
        ans = b
    else:
        s = ""
        s += str(int(b[0]) + 1)
        for i in range(size - 1):
            s += '0'
        for i in range(int(b), int(s) + 1):
            q = str(i)
            if len(set(q)) <= 2:
                ans1 = i
                break
        int_b = int(b)
        while int_b > 0:
            q = str(int_b)
            qq = set(q)
            if len(qq) <= 2:
                ans2 = int_b
                break
            int_b -= 1
  
        print(ans1, ans2)
        print(int_b)
        dist1 = abs(c - ans1)
        dist2 = abs(c - ans2)
        print(dist1, dist2)
        if dist1 < dist2:
            ans = ans1
        else:
            ans = ans2
  
  
    print(ans)
    output_file.write(str(ans) + "\n")
  
    input_file.close()
    output_file.close()
  
  
if __name__ == "__main__":
    main()
