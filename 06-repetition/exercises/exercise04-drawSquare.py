line = int(input("How many lines : "))

for i in range(line):
    if i == 0 or i == line - 1:
        print("*" * line)
    else:
        print("*" + " " * (line - 2) + "*")
    