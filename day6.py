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


if __name__ == "__main__":
    # data = get_input("test.txt")
    data = get_input("day6.txt")
    answers = unique_answers(data)
    solution1(answers)
