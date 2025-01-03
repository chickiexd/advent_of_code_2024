from input import get_input_data_as_list, get_input_data_as_string
from functools import cache


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_string
    towels, combinations = input.split("\n\n")
    towels = towels.split(", ")
    combinations = combinations.split("\n")

    @cache
    def find_solution(combination):
        if combination == "":
            return True
        return any(
            combination.startswith(t) and find_solution(combination[len(t) :])
            for t in towels
        )

    res = 0
    for c in combinations:
        res += find_solution(c)
    print(res - 1)


if __name__ == "__main__":
    main()
