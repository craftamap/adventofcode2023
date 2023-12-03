import sys
import math

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

coordinates_of_gears = set()

for y in range(len(lines)):
    for x in range(len(lines[0])):
        value = lines[y][x]
        if value == "*":
            coordinates_of_gears.add((y,x))

potential_number_coordinates = set()
gear_to_number_coordinates = {}
for symbol in coordinates_of_gears:
    for dy in [-1,0,1]:
        for dx in [-1,0,1]:
            value: str = l_g(l_g(lines, symbol[0]+dy, []), symbol[1]+dx, '.')
            if (value.isnumeric()):
                potential_number_coordinates.add((symbol[0]+dy, symbol[1]+dx))
                a = gear_to_number_coordinates.get(symbol, [])
                a.append((symbol[0]+dy, symbol[1]+dx))
                gear_to_number_coordinates[symbol] = a

gear_ratios = []
for number_coordinates_for_gear in gear_to_number_coordinates.values():
    numerics = []
    ncg = set(number_coordinates_for_gear)
    while len(ncg) > 0:
        pos = ncg.pop()
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
                if numeric_pos in ncg:
                    ncg.remove(numeric_pos)
                numeric_pos = (numeric_pos[0], numeric_pos[1]+1)
            else: 
                break
        numerics.append(int(numeric))

    if (len(numerics) == 2):
        gear_ratios.append(math.prod(numerics))
print(sum(gear_ratios))
