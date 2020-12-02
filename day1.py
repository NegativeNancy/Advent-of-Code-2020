fhand = open('input/day1.txt')

num_list = []

for line in fhand:
    numbers = line.split()
    for number in numbers:
        num_list.append(number)

for item in num_list:
    for num in num_list:
        for digit in num_list:
            addition = int(num) + int(item) + int(digit)
            if addition == 2020:
                result = int(num) * int(item) * int(digit)
                print(result)