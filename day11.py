def get_input(location):
    location = "input/" + location

    with open(location) as fhand:
        for line in fhand:
           continue

    return layout


def solution1(data):
    pass


def solution2(data):
    pass


if __name__ == "__main__":
    FILENAME = "test.txt"
    # FILENAME = "day11.txt"

    solution1(get_input(FILENAME))
    solution2(get_input(FILENAME))