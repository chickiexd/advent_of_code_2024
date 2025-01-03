from input import get_input_data_as_list, get_input_data_as_string


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_string
    registers, program = input.split("\n\n")
    registers_list = registers.split("\n")
    original_registers = {}
    original_registers["a"] = int(registers_list[0].split(":")[1])
    original_registers["b"] = int(registers_list[1].split(":")[1])
    original_registers["c"] = int(registers_list[2].split(":")[1])

    program = [int(x) for x in program.split(":")[1].rstrip("\n").split(",")]

    def run(a):
        def combo(x):
            match x:
                case 4:
                    return registers["a"]
                case 5:
                    return registers["b"]
                case 6:
                    return registers["c"]
            return x

        registers = original_registers.copy()
        registers["a"] = a
        i = 0
        output = []
        while i < len(program):
            opcode, operand = program[i], program[i + 1]
            match opcode:
                case 0:
                    registers["a"] = int(registers["a"] / 2 ** combo(operand))
                case 1:
                    registers["b"] = int(registers["b"] ^ operand)
                case 2:
                    registers["b"] = int(combo(operand) % 8)
                case 3:
                    if registers["a"] != 0:
                        i = operand - 2
                case 4:
                    registers["b"] = int(registers["b"] ^ registers["c"])
                case 5:
                    output.append(combo(operand) % 8)
                case 6:
                    registers["b"] = int(registers["a"] / 2 ** combo(operand))
                case 7:
                    registers["c"] = int(registers["a"] / 2 ** combo(operand))
            i += 2
        return output

    a = 1
    res = float("inf")
    while len(run(a)) <= len(program) and a < res:
        a = a << 1
        for i in reversed(range(len(program))):
            while run(a) != program[i:]:
                a += 1
            if run(a) == program:
                print(a)
                res = a
            a = a << 3


if __name__ == "__main__":
    main()
