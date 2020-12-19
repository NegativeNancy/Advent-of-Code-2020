import string

def get_input(input):
    with open(input) as fhand:
        data = fhand.readlines()
        
    return data
    

def split_input(data):
    new_line = ""
    new_data = ""
    counter = 0
    passports = 0

    for line in data:
        if len(line) > 1 and not (len(data) == (counter + 1)):
            new_line += line.strip() + ' '
        elif len(data) == (counter + 1):
            new_line += line.strip()
            new_data += (new_line + '\n\n')
            passports += 1
        else:
            new_data += new_line + '\n\n'
            passports += 1
            new_line = ""
        counter += 1

    print("Total passports:", passports)
    
    return new_data
    

def sort_data(data):
    new_line = ""
    words = [word.lower() for word in data.split()]
    words.sort()
    for word in words:
        new_line += word + " "
    return new_line


def validate_input(data):
    check_for = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    check_for_min = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_count = 0 

    for line in data.splitlines():
        new_line = ''
        new_line = sort_data(line)
        
        if len(new_line) > 1 and all(x in new_line for x in check_for):
            if (check_validity(new_line) == True):
                valid_count += 1
        elif len(new_line) > 1 and all(x in new_line for x in check_for_min):
            if (check_validity(new_line) == True):
                valid_count += 1

    return valid_count


def check_validity(data):
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False
    hexa = string.hexdigits

    for line in data.split():
        if "byr" in line:
            if (int(get_value(line)) >= 1920) and (int(get_value(line)) <= 2002):
                byr = True
        elif "iyr" in line:
            if (int(get_value(line)) >= 2010) and (int(get_value(line)) <= 2020):
                iyr = True 
        elif "eyr" in line:
            if (int(get_value(line)) >= 2020) and (int(get_value(line)) <= 2030):
                eyr = True
        elif "hgt" in line:
            value = get_value(line)
            if (value[-2:] == "cm") and (len(value) == 5) and ((int(value[:3]) >= 150) and (int(value[:3]) <= 193)):
                hgt = True
            elif (value[-2:] == "in") and (len(value) == 4) and ((int(value[:2]) >= 59) and (int(value[:2]) <= 76)):
                hgt = True
        elif "hcl" in line:
            value = get_value(line)
            counter = 0
            is_hex = False
            for char in value:
                if (counter > 0) and (char in hexa):
                    is_hex = True   
                counter += 1
            if (value[:1] == "#") and (len(value[1:]) == 6) and (is_hex == True):
                hcl = True
        elif "ecl" in line:
            value = get_value(line)
            if (value in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}):
                ecl = True
        elif "pid" in line:
            value = get_value(line)
            if (len(value) == 9) and value.isnumeric() == True:
                pid = True
                
    if (byr == True) and (iyr == True) and (eyr == True) and (hgt == True) and (hcl == True) and (ecl == True) and (pid == True):
        return True
    else:
        return False


def get_value(data):
    return (data[4:])


if __name__ == "__main__":
    data = get_input("input/day4.txt")

    corrected_data = split_input(data)
    valid_count = validate_input(corrected_data)
    print("Total valid passports:", valid_count)
