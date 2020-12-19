def get_input(location):
    location = "input/" + location
    numbers = []

    with open(location) as fhand:
        for line in fhand:
            number = line.strip()
            numbers.append(int(number))
    
    numbers.append(max(numbers) + 3)
    numbers.append(0)
    numbers.sort()

    return numbers


def use_every_adapter(data):
    i = 0
    total = 0
    one_jolt_used = []
    three_jolt_used = []
    adapters_used = []

    while total < (LAPTOP_ADAPTER - 3) and (i < len(data)):
        if (data[i]) == (total + 1):
            total = data[i]
            one_jolt_used.append(data[i])
            adapters_used.append(data[i])
            i += 1
        elif (data[i]) == (total + 3):
            total = data[i]
            three_jolt_used.append(data[i])
            adapters_used.append(data[i])
            i += 1
        else:
            i += 1
        
    if (total == (LAPTOP_ADAPTER - 3)):
        return (len(one_jolt_used) * len(three_jolt_used))


def get_unique_combos(data):
    unique_combo = {}

    for adapter in data:
        if adapter == min(data):
            unique_combo[adapter] = 1
        else:
            valid1 = unique_combo.get(adapter - 1, 0)
            valid2 = unique_combo.get(adapter - 2, 0)
            valid3 = unique_combo.get(adapter - 3, 0)
            unique_combo[adapter] = valid1 + valid2 + valid3
    return max(unique_combo.values())


def solution1(data):
    print("Laptop adapter Jolts:", LAPTOP_ADAPTER)
    print("number of 1-jolt differences multiplied by the number of 3-jolt differences:", use_every_adapter(data))


def solution2(data):
    print("Number of valid combinations:", get_unique_combos(data))


if __name__ == "__main__":
    # FILENAME = "test.txt"
    FILENAME = "day10.txt"
    LAPTOP_ADAPTER = (max(get_input(FILENAME)) + 3)

    solution1(get_input(FILENAME))
    solution2(get_input(FILENAME))
    