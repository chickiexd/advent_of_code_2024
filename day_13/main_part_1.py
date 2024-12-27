from input import get_input_data_as_list, get_input_data_as_string


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_list_test

    button_a = []
    button_b = []
    prize = []

    for i in range(0, len(input), 4):
        button_a.append(
            (
                int(input[i].split(" ")[2].rstrip(",").lstrip("X+")),
                int(input[i].split(" ")[3].rstrip(",").lstrip("Y+")),
            )
        )

    for i in range(1, len(input), 4):
        button_b.append(
            (
                int(input[i].split(" ")[2].rstrip(",").lstrip("X+")),
                int(input[i].split(" ")[3].rstrip(",").lstrip("Y+")),
            )
        )

    for i in range(2, len(input), 4):
        prize.append(
            (
                int(input[i].split(" ")[1].rstrip(",").lstrip("X=")),
                int(input[i].split(" ")[2].rstrip(",").lstrip("Y=")),
            )
        )

    def get_min_token_to_prize(a, b, prize):
        max_bx = prize[0] / b[0]
        max_by = prize[1] / b[1]
        max_b = int(min(max_bx, max_by))

        for i in range(max_b, 0, -1):
            crnt_x, crnt_y = tuple(x * i for x in b)
            missing_x, missing_y = prize[0] - crnt_x, prize[1] - crnt_y
            if missing_x % a[0] == 0 and missing_y % a[1] == 0:
                if missing_x / a[0] == missing_y / a[1]:
                    return int(i + missing_y / a[1] * 3)
        return 0

    res = 0
    for i in range(len(button_a)):
        r = get_min_token_to_prize(button_a[i], button_b[i], prize[i])
        res += r
    print(res)
    pass


if __name__ == "__main__":
    main()
