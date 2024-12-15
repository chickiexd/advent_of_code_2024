from input import get_input_data_as_list, get_input_data_as_string
from itertools import product


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_list

    input = [x.split(":") for x in input]
    res = [x[0] for x in input]
    numbers = [x[1].lstrip(" ").split(" ") for x in input]

    def generate_combinations(l):
        return list(product(["+", "*"], repeat=l))

    final = 0
    for i in range(len(res)):
        operands = generate_combinations(len(numbers[i]) - 1)
        for combination in operands:
            x = int(numbers[i][0])
            for j in range(1, len(numbers[i])):
                if combination[j - 1] == "+":
                    x += int(numbers[i][j])
                if combination[j - 1] == "*":
                    x = x * int(numbers[i][j])
            if x == int(res[i]):
                final += x
                break

    print(final)


if __name__ == "__main__":
    main()
