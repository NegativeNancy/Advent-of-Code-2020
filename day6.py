def get_input(location):
    location = "input/" + location
    with open(location) as fhand:
        data = [line.strip() for line in fhand]
       
    return data


def unique_answers(data):
    total = 0
    counter = 0
    new_line = ""
    for line in data:
        if (len(data) == (counter + 1)):
            new_line += line
            total = total_answers(total, new_line)
        elif (line.isalpha() == True):
            new_line += line
        else:
            total = total_answers(total, new_line)
            new_line = ""
        counter += 1
    
    return total


def total_answers(total, new_line):
    unique = set(new_line)
    total += len(unique)
    return total


def solution1(answers):
    print("Total of submited answers:", answers)


def duplicate_answers(data):
    duplicate = 0
    group_size = len(data.splitlines())

    for char in set(data) :
        if (char.isalpha() == True):
            counts = data.count(char)
            if (counts == group_size):
                duplicate += 1
    return duplicate


def get_group(data):
    counter = 0
    group_data = {}
    temp_data = ''

    for line in data:
        if (len(data) == counter + 1):
            temp_data += line + "\n"
            group_data[counter] = temp_data
        elif (line.isalpha() == True):
            temp_data += line + "\n"
            counter += 1
        else:
            group_data[counter] = temp_data
            temp_data = ''
            counter += 1
    
    return group_data


def solution2(group_data):
    total = 0
    for value in group_data.values():
        total += duplicate_answers(value)
    print("Sum of questions where all group members answered with yes:", total)


if __name__ == "__main__":
    # data = get_input("test.txt")
    data = get_input("day6.txt")
    solution1(unique_answers(data))
    solution2(get_group(data))
    