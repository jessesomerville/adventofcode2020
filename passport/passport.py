
with open('input.txt', 'r') as f:
    passports = f.read().split('\n\n')

required = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
valid = 0
for passport in passports:
    mapped = dict(pp.split(':') for pp in passport.split())
    if all(field in mapped.keys() for field in required):
        valid += 1

print(valid)