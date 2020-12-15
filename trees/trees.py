with open('input.txt', 'r') as f:
    slope_map = [l.strip() for l in f.readlines()]

length = len(slope_map)
line_len = len(slope_map[0])

widen_to = length * 3

widened = []
for line in slope_map:
    orig_line = line
    while len(line) < widen_to:
        line += orig_line
    widened.append(line)

x = [0, 0]
total_hits = 0
try:
    while True:
        if widened[x[0]][x[1]] == '#':
            total_hits += 1
        x[0] += 1
        x[1] += 3
except:
    print(total_hits)