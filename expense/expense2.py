with open('input.txt', 'r') as f:
    lines = [int(l.strip()) for l in f.readlines()]

for num in lines:
    sums = [s + num for s in lines]
    third = [x for y in sums for x in lines if x + y == 2020]
    if len(third) > 0:
        print(f'num: {num} third: {third}')