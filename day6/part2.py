import sys
import math

file = sys.argv[1]

with open(file) as fh:
    lines = fh.readlines()

times = int(lines[0].split(None, 1)[1].replace(' ', ''))
distances = int(lines[1].split(None, 1)[1].replace(' ', ''))

timings = [[times, distances]] 

fasterinos = []
for x in timings:
    time = x[0]
    record_distance = x[1]
    faster = 0
    for x in range(time+1):
        button_time = x
        drive_time = time - x
        speed = button_time
        distance = speed * drive_time
        if distance > record_distance:
            faster += 1
    fasterinos.append(faster)

print(math.prod(fasterinos))
