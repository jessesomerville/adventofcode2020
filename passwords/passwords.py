with open('input.txt', 'r') as f:
    lines = [l.split() for l in f.readlines()]

total = 0
for pol in lines:
    num_of_occ = pol[2].count(pol[1][0])
    min_count, max_count = pol[0].split('-')
    min_count = int(min_count)
    max_count = int(max_count)

    if min_count <= num_of_occ <= max_count:
        print(min_count, num_of_occ, max_count)
        total += 1

print(total)