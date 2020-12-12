def get_input(location):
    location = "input/" + location
    bags = {}
    with open(location) as fhand:
        for line in fhand:
            bag, contains = line.split(" bags contain ") 
            colors = []
            for color in contains.split(','):
                color = color.strip()
                color = color.strip("bags.")
                colors.append(color)
            bags[bag] = colors
       
    return bags


def can_contain(bags, color, contains):
    for bag in bags:
        for value in bags.get(bag):
            if value[2:].strip() == color:
                new_color = bag
                contains.append(bag) if bag not in contains else contains
                can_contain(bags, new_color, contains)
    
    return contains


def solution1(bags):
    print("Number of bags that can contain \'shiny gold\' bags:", len(can_contain(bags, "shiny gold", [])))
    

def solution2(bags):
    pass


if __name__ == "__main__":
    # bags = get_input("test.txt")
    bags = get_input("day7.txt")
    solution1(bags)
    # solution2()