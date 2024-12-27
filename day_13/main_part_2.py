from input import get_input_data_as_list, get_input_data_as_string


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_list

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
                int(input[i].split(" ")[1].rstrip(",").lstrip("X=")) + 10000000000000,
                int(input[i].split(" ")[2].rstrip(",").lstrip("Y=")) + 10000000000000,
            )
        )

    def get_min_token_to_prize(a, b, prize):
        ax, ay = a
        bx, by = b
        px, py = prize
        a_count = (px * by - py * bx) / (ax * by - ay * bx)
        b_count = (px - ax * a_count) / bx
        if a_count % 1 == 0 and b_count % 1 == 0:
            return int(b_count + a_count * 3)
        return 0

    res = 0
    for i in range(len(button_a)):
        r = get_min_token_to_prize(button_a[i], button_b[i], prize[i])
        res += r
    print(res)


if __name__ == "__main__":
    main()
