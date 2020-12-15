from functools import reduce

with open('input.txt', 'r') as f:
    slope_map = [l.strip() for l in f.readlines()]

length = len(slope_map)
line_len = len(slope_map[0])

widen_to = length * 7

widened = []
for line in slope_map:
    orig_line = line
    while len(line) < widen_to:
        line += orig_line
    widened.append(line)

angles = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]
all_hits = []
for angle in angles:
    x = [0, 0]
    total_hits = 0
    try:
        while True:
            if widened[x[0]][x[1]] == '#':
                total_hits += 1
            x[0] += angle[1]
            x[1] += angle[0]
    except:
        all_hits.append(total_hits)
        print(f'{angle}: {total_hits}')

print(f'Answer: {reduce(lambda x, y: x * y, all_hits)}')