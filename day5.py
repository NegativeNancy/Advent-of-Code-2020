def get_input(location):
    location = "input/" + location
    with open(location) as fhand:
        data = [line.strip() for line in fhand]
    return data


def find_place(line, lower, upper):
    if (lower == "F") or (upper == "F"):
        minimum = 0
        maximum = 127
    else:
        minimum = 0
        maximum = 7

    for char in line:
        if (char == lower):
            minimum = int(new_value(minimum, maximum))
        elif (char == upper):
            maximum = int(new_value(minimum, maximum))

    return maximum


def new_value(mi, ma):
    if (mi == 0):
        return (ma / 2)
    elif (mi > 0):
        new_value = (mi + ma)
        return (int(new_value) / 2)


def find_seat_id(row, column):
    return row * 8 + column


def solve1(seats):
    print("Highest seat ID:", max(seats))


def solve2(seats):
    for seat in seats:
        next_seat = (seat + 1)
        if (next_seat not in seats) and (next_seat < len(seats)):
            print("My seat is:", (next_seat))


if __name__ == "__main__":
    # data = get_input("test.txt")
    data = get_input("day5.txt")
    
    seats = []
    for line in data:    
        row = find_place(line, "B", "F")    
        column = find_place(line, "R", "L")
        seats.append(find_seat_id(row, column))

    seats = sorted(seats)
    
    solve1(seats)
    solve2(seats)