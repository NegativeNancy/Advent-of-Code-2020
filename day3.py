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

def show_path(x, y, data):
    row = 0
    trees_hit = 0
    next_x = x
    next_y = y
 
    for line in data:
        if row == next_y:
            line = line.strip()
            new_line = ""
            char_count = 0
            original_line = line

            while next_x >= len(line):
                line = line + original_line 
            for char in line:
                if char_count == next_x and next_x > 0:
                    if char == ".":
                        char = "O"
                    elif char == "#":
                        char = "X"
                        trees_hit += 1
                new_line = new_line + char
                char_count += 1
            # print(new_line)
            next_x += x
            next_y += y
        row += 1

    print("Total trees hit: ", trees_hit)
    return trees_hit

    
if __name__ == "__main__":
    START_POS = 0
    inputFile = "input/day3.txt"
    data = get_input(inputFile)

    trees_hit = []

    trees_hit.append(show_path(1, 1, data))
    trees_hit.append(show_path(3, 1, data))
    trees_hit.append(show_path(5, 1, data))
    trees_hit.append(show_path(7, 1, data))
    trees_hit.append(show_path(1, 2, data))

    total = 1

    for run in trees_hit:
        total = total * run 

    print("Trees hit:", total)