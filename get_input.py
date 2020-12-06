def get_input(input):
    data = []
    length = 0

    with open(input) as fhand:
        data = fhand.readlines()
        length = int(len(data))
    
    for line in data:
        line = line.strip()
        line += line * 4
    
    print("Data size is:", length, "lines")

    return data