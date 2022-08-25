with open("INPUT.TXT", 'r') as input_file:
    data = input_file.readline().split()
  
M, Y, X = int(data[1]), int(data[2]), int(data[3])
  
with open("OUTPUT.TXT", 'w') as output_file:
    if Y % 2 == 0:
        output_file.write(f"{(((Y * M) - 1) - M + 1) + (M - X)}")
    else:
        output_file.write(f"{((Y * M) - 1) - (M - X)}")
