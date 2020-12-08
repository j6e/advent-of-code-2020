import re
from typing import List
"""
Expected fields

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

Your job is to count the passports where all required fields are 
both present and valid according to the above rules. 
"""

regexes = {
    "byr": r"byr:(\d{4})\s", 
    "iyr": r"iyr:(2010|2011|2012|2013|2014|2015|2016|2017|2018|2019|2020)\s", 
    "eyr": r"eyr:(2020|2021|2022|2023|2024|2025|2026|2027|2028|2029|2030)\s", 
    "hgt": r"hgt:(\d+)(cm|in)\s", 
    "hcl": r"hcl:(#[0-9a-f]{6})\s", 
    "ecl": r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\s", 
    "pid": r"pid:(\d{9})\s"
}


def validate_byr(passport: str) -> bool: 
    matches = re.findall(regexes["byr"], passport, re.MULTILINE)
    if len(matches) != 1:
        return False
    elif matches[0] < "1920" or matches[0] > "2002":
        return False
    else:
        return True


def validate_hgt(passport: str) -> bool: 
    matches = re.findall(regexes["hgt"], passport, re.MULTILINE)
    if len(matches) != 1:
        return False
    height, unit = int(matches[0][0]), matches[0][1]
    if unit == "cm":
        if height < 150 or height > 193:
            return False
        else:
            return True 
    elif unit == "in":
        if height < 59 or height > 76:
            return False
        else:
            return True
    else:
        return False

def validate_regex(passport: str, regex: str) -> bool:
    matches = re.findall(regex, passport, re.MULTILINE)
    if len(matches) == 1:
        return True
    else:
        return False

def validate_iyr(passport: str) -> bool:
    return validate_regex(passport, regexes['iyr'])


def validate_eyr(passport: str) -> bool:
    return validate_regex(passport, regexes['eyr'])


def validate_hcl(passport: str) -> bool:
    return validate_regex(passport, regexes['hcl'])


def validate_ecl(passport: str) -> bool:
    return validate_regex(passport, regexes['ecl'])


def validate_pid(passport: str) -> bool:
    return validate_regex(passport, regexes['pid'])



def validate_passport(passport: str) -> bool:
    print(passport)

    byr = validate_byr(passport)
    iyr = validate_iyr(passport)    
    eyr = validate_eyr(passport)
    hgt = validate_hgt(passport)
    hcl = validate_hcl(passport)
    ecl = validate_ecl(passport)
    pid = validate_pid(passport)

    if all([byr, iyr, eyr, hgt, hcl, ecl, pid]):
        print('ALL VALID')
        return True
    else:
        print(f"byr: {byr}, iyr: {iyr}, eyr: {eyr}, hgt: {hgt}, hcl: {hcl}, ecl: {ecl}, pid: {pid}")
        return False    


def parse_blocks(text: str) -> List[str]:
    res = [passport.replace('\n', ' ') + ' ' for passport in text.split('\n\n')]
    return res


def read_file(file: str) -> str:
    with open(file, 'r') as f:
        lines = f.readlines() 
    text = ''.join(lines)
    return text

if __name__ == "__main__":
    fname = 'advent_of_code/04_passport_processing/input.txt'
    text = read_file(fname)
    l_passports = parse_blocks(text)
    valids = []
    for i, passport in enumerate(l_passports):
        print(f'-- {i:03} --')
        valids.append(validate_passport(passport))
    print('----')
    print(f'{sum(valids)} valid passaports')
