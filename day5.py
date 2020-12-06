def get_input(location):
    location = "input/" + location
    with open(location) as fhand:
        data = fhand.readlines()

    new_data = []
    for line in data:
        new_data.append(line.strip())
    return new_data


def find_row(data):
    minimum = 0
    maximum = 127

    for char in line:
        if (char == "B"):
            minimum = int(new_value(minimum, maximum))
        elif (char == "F"):
            maximum = int(new_value(minimum, maximum))

    return maximum


def find_column(data):
    minimum = 0
    maximum = 7

    for char in line:
        if (char == "R"):
            minimum = int(new_value(minimum, maximum))
        elif (char == "L"):
            maximum = int(new_value(minimum, maximum))

    return maximum


def new_value(mi, ma):
    if (mi == 0):
        return (ma / 2)
    elif (mi > 0):
        new_value = (mi + ma)
        return (int(new_value) / 2)


def find_seat_id(row, column):
    seat = row * 8 + column
    return seat


def find_my_seat(seats):
    for seat in seats:
        next_seat = (seat + 1)
        if (next_seat not in seats) and (next_seat < len(seats)):
            print("My seat is:", (next_seat))


if __name__ == "__main__":
    # data = get_input("test.txt")
    data = get_input("day5.txt")
    
    seats = []
    highest = 0
    for line in data:        
        seat = find_seat_id(find_row(line),find_column(line))
        seats.append(seat)
        if (int(seat) > highest):
            highest = seat
    
    print("Highest seat ID:", highest)
    seats_1 = sorted(seats)
    find_my_seat(seats_1)
