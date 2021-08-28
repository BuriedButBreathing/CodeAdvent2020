import re
filepath = "C:\\users\\higgi\\onedrive\\documents\\github\\codeadvent2020\\question4\\input.txt"

with open(filepath) as r:
    # content = r.read().split('\n')
    content = r.read().split(',')
    
# valid_count = 0
# required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# def passport_validation(passport):
#     for field in required_fields:
#         if field not in passport:
#             return False
#     return True

# for passport in content:
#     if passport_validation(passport):
#         valid_count += 1
# print(valid_count)


# Part 2

valid_count = 0
def passport_parser(content_line):
    passport_dictionary = {}
    passport_split = content_line.split(' ')
    for item in passport_split:
        values = item.split(":")
        passport_dictionary[values[0]] = values[1]
    return passport_dictionary

def birth_year_check(passport):
    if passport['byr']:
        birth_year = int(passport['byr'])
        if birth_year > 1920 and birth_year < 2002:
            return True
        else:
            return False
    else:
        return False

def issue_year_check(passport):
    issue_year = int(passport['iyr'])
    if issue_year > 2010 or issue_year < 2020:
        return True
    else:
        return False

def expiration_year_check(passport):
    expiration_year = int(passport['eyr'])
    if expiration_year > 2020 or expiration_year < 2030:
        return True
    else:
        return False
def height_check(passport):
    if 'in' in passport['hgt']:
        hgt_comp = int(passport['hgt'].strip('in'))
        if hgt_comp > 59 or hgt_comp < 76:
            return True
        else:
            return False
    if 'cm' in passport['hgt']:
        hgt_comp = int(passport['hgt'].strip('cm'))
        if hgt_comp > 150 or hgt_comp < 193:
            return True
        else:
            return False
def hair_color_check(passport):
    hair_match = re.compile(r'#(?:[0-9a-fA-F]{3}){1,2}')
    if hair_match.match(passport['hcl']):
        return True
    else:
        return False

def eye_color_check(passport):
    approved_colors = 'amb blu brn gry grn hzl oth'
    if passport['ecl'] not in approved_colors:
        return False
    else:
        return True
def passport_id_check(passport):
    pid = passport['pid']
    if pid.isnumeric() and len(pid) == 9:
        return True
    else:
        return False

def validate_fields(passport):
    birth_check =birth_year_check(passport)
    issue_check = issue_year_check(passport)
    expire_check = expiration_year_check(passport)
    hgt_check = height_check(passport)
    hair_check = hair_color_check(passport)
    eye_check = eye_color_check(passport)
    pass_check = passport_id_check(passport)
    if birth_check == True and issue_check == True and expire_check == True and hgt_check == True and hair_check == True and eye_check == True and pass_check == True:
        return True
    else:
        return False



test_dict = {'eyr': '2030', 'pid': '039638764', 'ecl': 'hzl', 'hgt': '190 cm', 'byr': '1926', 'cid': '294', 'hcl': '#b6652a', 'iyr': '2017'}



# print(birth_year_check(test_dict), issue_year_check(test_dict), expiration_year_check(test_dict), height_check(test_dict), hair_color_check(test_dict), eye_color_check(test_dict), passport_id_check(test_dict))

valid_count = 0
for line in content:
    passport = passport_parser(line)
    check_result = validate_fields(passport)
    if check_result:
        valid_count += 1
print(valid_count)