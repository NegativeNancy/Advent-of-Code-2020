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

def run_machine_code(instructions):
    accumulator = 0
    counter = 0
    
    while counter < len(instructions):
        if ("acc" in instructions[counter].keys()) and (len(instructions[counter]) == 1):
            accumulator = eval(str(accumulator) + instructions[counter].get("acc"))
            done = {"done": "done"}
            instructions[counter].update(done)
            counter += 1
        elif "jmp" in instructions[counter].keys() and (len(instructions[counter]) == 1):
            jump = eval(str(counter) + instructions[counter].get("jmp"))
            counter = jump
        elif "nop" in instructions[counter].keys() and (len(instructions[counter]) == 1):
            counter += 1
        elif (len(instructions[counter]) > 1):
            return accumulator

def solution1(instructions):
    print("Accumulator:", run_machine_code(instructions))

def solution2(instructions):
    pass

if __name__ == "__main__":
    # instructions = get_input("test.txt")
    instructions = get_input("day8.txt")
    solution1(instructions)
    solution2(instructions)