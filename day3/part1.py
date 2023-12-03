import sys

def l_g(lis, idx, default):
    if (idx < 0):
        return default
    slice = lis[idx:idx+1]
    if (len(slice) > 0):
        return slice[0]
    return default
    

file = sys.argv[1]

with open(file) as fh:
    lines = [x.strip() for x in fh.readlines()]

# find symbols

coordinates_of_symbols = []

for y in range(len(lines)):
    for x in range(len(lines[0])):
        value = lines[y][x]
        if value != "." and not value.isnumeric():
            coordinates_of_symbols.append((y,x))

potential_number_coordinates = set()
for symbol in coordinates_of_symbols:
    for dy in [-1,0,1]:
        for dx in [-1,0,1]:
            value: str = l_g(l_g(lines, symbol[0]+dy, []), symbol[1]+dx, '.')
            if (value.isnumeric()):
                potential_number_coordinates.add((symbol[0]+dy, symbol[1]+dx))


numerics = []
while len(potential_number_coordinates) > 0:
    pos = potential_number_coordinates.pop()
    first_numeric = pos
    while True:
        value = l_g(l_g(lines, first_numeric[0], []), first_numeric[1] - 1, '.')
        if (value.isnumeric()):
            first_numeric = (first_numeric[0], first_numeric[1] - 1)
        else:
            break
    numeric = ''
    numeric_pos = first_numeric
    while True:
        v = l_g(l_g(lines, numeric_pos[0], []), numeric_pos[1], '.')
        if (v.isnumeric()):
            numeric += v
            if numeric_pos in potential_number_coordinates:
                potential_number_coordinates.remove(numeric_pos)
            numeric_pos = (numeric_pos[0], numeric_pos[1]+1)
        else: 
            break
    numerics.append(int(numeric))

print(sum(numerics))
