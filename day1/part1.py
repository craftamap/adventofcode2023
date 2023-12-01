import sys

file = sys.argv[1]

with open(file) as fh:
    lines = fh.readlines()

sum = 0
for line in lines:
    line_digits = ''
    for i in range(0, len(line)):
        if line[i].isnumeric():
            line_digits += line[i]
            break
    for i in range(len(line)-1, -1, -1):
        if line[i].isnumeric():
            line_digits += line[i]
            break
    sum += int(line_digits)
print(sum)
