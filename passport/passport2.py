import re

with open('input.txt', 'r') as f:
    passports = f.read().split('\n\n')

required = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
valid = 0
for passport in passports:
    mapped = dict(pp.split(':') for pp in passport.split())
    if not all(field in mapped.keys() for field in required):
        continue

    byr = mapped['byr'].isdigit() and 1920 <= int(mapped['byr']) <= 2020
    iyr = mapped['iyr'].isdigit() and 2010 <= int(mapped['iyr']) <= 2020
    eyr = mapped['eyr'].isdigit() and 2020 <= int(mapped['eyr']) <= 2030
    hcl = bool(re.search(r'^#[a-f0-9]{6}$', mapped['hcl']))
    ecl = mapped['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    pid = bool(re.search(r'^[\d]{9}$', mapped['pid']))

    hgt = False
    if match := re.search(r'^([\d]{2,3})(cm|in)$', mapped.get('hgt')):
        if match.group(2) == 'cm':
            if 150 <= int(match.group(1)) <= 193:
                hgt = True
        else:
            if 59 <= int(match.group(1)) <= 76:
                hgt = True
    if all([ecl, pid, eyr, hcl, byr, iyr, hgt]):
        valid += 1

print(valid)