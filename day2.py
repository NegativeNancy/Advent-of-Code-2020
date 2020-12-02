fhand = open('input/day2.txt')

data = []

for line in fhand:
    data.append(line.split())

total1 = 0
total2 = 0

for line in data:
    minimum = int(line[0][:line[0].index('-')])
    maximum = int(line[0][line[0].index('-') + 1:])
    required = line[1][:1]
    # print('Minimum: %s, Maximum: %s, Required: %s' %(minimum, maximum, required))

    counter = 0
    for char in line[2]:
        # print('Required char: %s, Got char: %s' %(required, char))
        if char == required:
            # print('Valid Char')
            counter += 1

    if counter >= minimum and counter <= maximum:
        total1 += 1
        # print('Password is valid.')
    # else:
        # print('Password is not valid.')
    

for line in data:
    minimum = int(line[0][:line[0].index('-')])
    maximum = int(line[0][line[0].index('-') + 1:])
    required = line[1][:1]
    # print('Minimum: %s, Maximum: %s, Required: %s' %(minimum, maximum, required))

    counter = 0
    position = 1

    used = False
    valid = False

    for char in line[2]:
        # print('Required char: %s, Got char: %s, On possition: %i' %(required, char, position))
        if char == required and used == False and (position == minimum or position == maximum):
            used = True
            valid = True
            # print('Valid Char')
        elif char == required and used == True and (position == minimum or position == maximum):
            valid = False
            # print('Not Valid Char')
        position += 1

    if valid == True:
        total2 += 1
        # print('Password is valid')
    # else:
    #     print('Password is not valid')


print('An total of %i passwords are valid.' %total1)
print('An total of %i passwords are valid for the toboggan rental.' %total2)