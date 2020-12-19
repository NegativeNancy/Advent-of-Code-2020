def get_input(location):
    location = "input/" + location
    instructions = {}
    counter = 0

    with open(location) as fhand:
        for line in fhand:
            inst, arg = line.strip().split(" ")
            instruction = [inst, int(arg), False]
            instructions[counter] = instruction
            counter += 1
    
    return instructions


def run_machine_code(instructions):
    accumulator = 0
    counter = 0
    
    while True:
        if counter not in instructions.keys():
            return accumulator, True
        
        line = instructions[counter]

        if (line[2]):
            return accumulator, False
        elif (line[0] == "acc"):
            accumulator += line[1]
            counter += 1
        elif (line[0] == "jmp"):
            counter += line[1]
        elif (line[0] == "nop"):
            counter += 1
        line[2] = True


def stop_the_loop(instructions, location):
    for key in instructions.keys():
        instruction = instructions[key]

        if (instruction[0] == "nop") and (instruction[1] > 0):
            instruction[0] = "jmp"
        elif (instruction[0] == "jmp"):
            instruction[0] = "nop"
        
        loop_broken = run_machine_code(instructions)
        if loop_broken[1]:
            return loop_broken[0]
        
        instructions = get_input(location)


def solution1(instructions):
    print("Accumulator solution 1:", run_machine_code(instructions)[0])


def solution2(instructions, filename):
    print("Accumulator solution 2:", stop_the_loop(instructions, filename))


if __name__ == "__main__":
    # filename = "test.txt"
    filename = "day8.txt"

    solution1(get_input(filename))
    solution2(get_input(filename), filename)