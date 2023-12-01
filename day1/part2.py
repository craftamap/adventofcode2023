import sys

file = sys.argv[1]

with open(file) as fh:
    lines = fh.readlines()

written_digits = ["empty_zero_offset_value", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

sum = 0
for line in lines:
    line_digits = ''
    b=False
    for i in range(0, len(line)):
        if line[i].isnumeric():
            line_digits += line[i]
            break
        for (j, written_digit) in enumerate(written_digits):
            if line[i:100].startswith(written_digit):
                b=True
                line_digits += f"{j}"
        if b:
            break
    b=False
    for i in range(len(line)-1, -1, -1):
        if line[i].isnumeric():
            line_digits += line[i]
            break
        for (j, written_digit) in enumerate(written_digits):
            if line[i:100].startswith(written_digit):
                b=True
                line_digits += f"{j}"
        if b:
            break
    print(line_digits)
    sum += int(line_digits)
print(sum)
