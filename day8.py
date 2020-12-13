def get_input(location):
    location = "input/" + location
    instructions = []
    with open(location) as fhand:
        for line in fhand:
            instruction = {}
            inst, arg = line.strip().split(" ")
            instruction[inst] = arg
            instructions.append(instruction)
    
    # print(instructions)
    return instructions

def run_machine_code(instructions, flag):
    accumulator = 0
    counter = 0
    old_counter = counter
    
    while counter < len(instructions):
        print(instructions[counter])
        if ("acc" in instructions[counter].keys()) and (len(instructions[counter]) == 1):
            accumulator = eval(str(accumulator) + instructions[counter].get("acc"))
            done = {"done": "done"}
            instructions[counter].update(done)
            old_counter = counter
            counter += 1
        elif "jmp" in instructions[counter].keys() and (len(instructions[counter]) == 1):
            jump = eval(str(counter) + instructions[counter].get("jmp"))
            old_counter = counter
            counter = jump
        elif "nop" in instructions[counter].keys() and (len(instructions[counter]) == 1):
            old_counter = counter
            counter += 1
        elif (len(instructions[counter]) > 1) and (flag == 1):
            return accumulator
        elif (len(instructions[counter]) > 1) and (flag == 2):
            accumulator, counter, old_counter = stop_endless(instructions, accumulator, counter, old_counter)

    return accumulator

def stop_endless(instructions, accumulator, counter, old_counter):
    print("Current instruction:", instructions[counter])
    print("Previous instruction:", instructions[old_counter])

    if ("nop" in instructions[old_counter].keys()):
        jump = eval(str(counter) + instructions[old_counter].get("nop"))
        old_counter = counter
        counter = jump
    elif ("jmp" in instructions[old_counter].keys()):
        done = {"done": "done"}
        instructions[old_counter].update(done)
        old_counter += 1
    elif ("acc" in instructions[old_counter].keys()):
        accumulator = eval(str(accumulator) + instructions[old_counter].get("acc"))
        done = {"done": "done"}
        instructions[old_counter].update(done)
        old_counter += 1
    
    return accumulator, counter, old_counter


def solution1(instructions):
    print("Accumulator solution 1:", run_machine_code(instructions, 1))

def solution2(instructions):
    print("Accumulator solution 2:", run_machine_code(instructions, 2))


if __name__ == "__main__":
    instructions = get_input("test.txt")
    # instructions = get_input("day8.txt")
    instructions2 = instructions
    # solution1(instructions)
    solution2(instructions2)