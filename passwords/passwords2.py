with open('input.txt', 'r') as f:
    lines = [l.split() for l in f.readlines()]

total = 0
for pol in lines:
    min_count, max_count = pol[0].split('-')
    min_count = int(min_count) - 1
    max_count = int(max_count) - 1

    pwd = pol[2]
    char = pol[1][0]
    if bool(pwd[min_count] == char) != bool(pwd[max_count] == char):
        print(min_count, max_count, char, pwd)
        total += 1

print(total)