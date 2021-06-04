FILEPATH = "../data/2015/01.txt"


def main():
    instructions = get_data(FILEPATH).strip()
    final_location = get_final_location(instructions)
    print(f"Santa ended up on floor: {final_location}.")
    first_point_in_basement = get_first_basement_entry(instructions)
    print(f"Instruction at index position: {first_point_in_basement} is where Santa entered the basement.")


def get_data(instructions):
    with open("../data/2015/01.txt", "r", encoding="utf-8") as f:
        return f.read()


def get_final_location(instructions):
    total_up = instructions.count("(")
    total_down = instructions.count(")")
    return (total_up - total_down)


def get_first_basement_entry(instructions):
    current_level = 0
    current_index = 0
    for instruction in instructions:
        current_index += 1
        if instruction == "(":
            current_level += 1
        elif instruction == ")":
            current_level -= 1
        if current_level < 0:
            return current_index


if __name__ ==  "__main__":
    main()
