def main():
    input_file = open("input.txt", "r")
    output_file = open("output.txt", "w")
    line = input_file.readline().split()
    n = int(line[0])
    a = []
  
    for i in range(n):
        line = input_file.readline().split()
        if len(str(line[1])) == 1:
            if str(line[1]) == "g":
                l = int(line[0]) * (10 ** 3)
            if str(line[1]) == "p":
                l = int(line[0]) * 16380 * (10 ** 3)
            if str(line[1]) == "t":
                l = int(line[0]) * (10 ** 6) * (10 ** 3)
  
        if len(str(line[1])) == 2:
            if str(line[1][1]) == "g":
                if str(line[1][0]) == "m":
                    l = int(line[0])
                if str(line[1][0]) == "k":
                    l = int(line[0]) * (10 ** 3) * (10 ** 3)
                if str(line[1][0]) == "M":
                    l = int(line[0]) * (10 ** 6) * (10 ** 3)
                if str(line[1][0]) == "G":
                    l = int(line[0]) * (10 ** 9) * (10 ** 3)
            if str(line[1][1]) == "p":
                if str(line[1][0]) == "m":
                    l = int(line[0]) * 16380
                if str(line[1][0]) == "k":
                    l = int(line[0]) * (10 ** 3) * 16380 * (10 ** 3)
                if str(line[1][0]) == "M":
                    l = int(line[0]) * (10 ** 6) * 16380 * (10 ** 3)
                if str(line[1][0]) == "G":
                    l = int(line[0]) * (10 ** 9) * 16380 * (10 ** 3)
            if str(line[1][1]) == "t":
                if str(line[1][0]) == "m":
                    l = int(line[0]) * (10 ** 6)
                if str(line[1][0]) == "k":
                    l = int(line[0]) * (10 ** 3) * (10 ** 6) * (10 ** 3)
                if str(line[1][0]) == "M":
                    l = int(line[0]) * (10 ** 6) * (10 ** 6) * (10 ** 3)
                if str(line[1][0]) == "G":
                    l = int(line[0]) * (10 ** 9) * (10 ** 6) * (10 ** 3)
        a.append((int(line[0]), str(line[1]), l))
    #a.sort(key=lambda x:x[2])
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j][2] > a[j + 1][2]:
                a[j], a[j + 1] = a[j + 1], a[j]
  
    print(a)
    print(a)
    for i in range(len(a)):
        output_file.write(str(a[i][0]) + " " + str(a[i][1]) + "\n")
  
  
  
    #output_file.write(str(0) + '\n')
    input_file.close()
    output_file.close()
  
  
if __name__ == "__main__":
    main()
