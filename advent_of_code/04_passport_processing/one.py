import re

"""
Expected fields
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
Count the number of valid passports - those that have all required fields.
Treat cid as optional. 
In your batch file, how many passports are valid?
"""

with open('advent_of_code/04_passport_processing/input.txt', 'r') as f:
    lines = f.readlines() + ['\n']

#regex = r"(\w+):"
regex = r"(byr|iyr|eyr|hgt|hcl|ecl|pid|cid)"

mandatory = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

accu_matches = []
valids = 0
for l in lines:
    if l == '\n': # blank line
        #print(accu_matches)
        no_present = mandatory - set(accu_matches)
        #print(len(no_present))
        if len(no_present) == 0:
            valids += 1
        accu_matches = []
        continue
    
    matches = re.findall(regex, l)
    accu_matches += matches

print(f'{valids} valid passaports')

