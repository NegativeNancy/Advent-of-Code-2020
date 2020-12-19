def get_input(location):
    location = "input/" + location
    numbers = {}
    counter = 1

    with open(location) as fhand:
        for line in fhand:
            number = line.strip()
            numbers[counter] = int(number)
            counter += 1
    
    return numbers


def sum_of_two(data, preamble):
    for key in data.keys():
        line = data[key]
        if (key > preamble):
            i = 1
            valid = False
            while (i < (preamble  + 1)) and not (valid):
                j = 1 
                while (j < (preamble  + 1) and not (valid)):
                    if (key - i == key - j):
                        j += 1
                        continue
                    else: 
                        answer = data[key - i] + data[key - j]
                        if (answer == line):
                            valid = True
                    j += 1
                i += 1
            
            if not (valid):
                return line


def sum_of_range(data, sol1, preamble):
    for key in data.keys():
        total = 0
        i = key
        values_used = []
        while (total < sol1) and (i <= len(data)):
            values_used.append(data[i])
            total += data[i]
            i += 1

        if (total == sol1):
            return (min(values_used) + max(values_used))


def solution1(data, preamble):
    print("First number that is not the sum of two of the previous 25 numbers:", sum_of_two(data, preamble) )


def solution2(data, preamble):
    print("Accumulator solution 2:", sum_of_range(data, sum_of_two(data, preamble), preamble))


if __name__ == "__main__":
    # filename = "test.txt"
    # preamble = 5
    filename = "day9.txt"
    preamble = 25

    solution1(get_input(filename), preamble)
    solution2(get_input(filename), preamble)