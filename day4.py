import get_input as d

def split_input(data):
    new_line = ""
    new_data = ""
    counter = 0
    empty_rows = 0

    for line in data:
        if len(line) > 1 and not len(data) == counter + 1:
            new_line += line.strip() + ' '
        elif len(data) == counter + 1:
            new_data += new_line + '\n\n'
        else:
            new_data += new_line + '\n\n'
            new_line = ""

        if len(line) == 1:
            empty_rows += 1
        counter += 1
    
    print("Total of empty rows:", empty_rows)
    return new_data
    

def validate_input(data):
    check_for = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    check_for_min = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    
    valid_count = 0 
    not_valid = 0

    for line in data.splitlines():
        new_line = ""
        # print("Before sort:", line)
        words = [word.lower() for word in line.split()]
        words.sort()
        for word in words:
            new_line += word + " "
        # print("After sort:", new_line)
        
        if len(new_line) > 1 and all(x in new_line for x in check_for):
            # print("The following password is valid:", new_line)
            valid_count += 1
        elif len(new_line) > 1 and all(x in new_line for x in check_for_min):
            # print("The following password is valid, but missing CID:", new_line)
            valid_count += 1
        elif len(new_line) > 1:
            print("The following password is not valid:", new_line)
            not_valid += 1
        else:
            # print("Something went wrong with this string:", line)
            pass

    print("Not valid:", not_valid)
    return valid_count


# def sort_data(data):
#     words = []
#     for line in data.split():
#         words += line.lower()  

#     words.sort()

#     for word in words:
#         print(word)


if __name__ == "__main__":
    data = d.get_input("input/day4.txt")
    # data = d.get_input("input/test.txt")

    corrected_data = split_input(data)
    # sort_data(corrected_data)
    # print(corrected_data)
    valid_count = validate_input(corrected_data)
    print("Total valid passports:", valid_count)
