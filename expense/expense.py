with open('input.txt', 'r') as f:
    lines = [int(l.strip()) for l in f.readlines()]

for num in lines:
    x = 2020 - num
    try:
        print(next(i for i in lines if i == x))
    except StopIteration:
        ...