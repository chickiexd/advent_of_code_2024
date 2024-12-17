from input import get_input_data_as_list, get_input_data_as_string


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_list
    input = input[0].split(" ")

    counter = 25
    while counter > 0:
        new_order = []
        for x in input:
            if x == "0":
                new_order.append("1")
            elif len(x) % 2 == 0:
                new_value = x[: int(len(x) / 2)].lstrip("0")
                if new_value == "":
                    new_order.append("0")
                else:
                    new_order.append(new_value)
                new_value = x[int(len(x) / 2) :].lstrip("0")
                if new_value == "":
                    new_order.append("0")
                else:
                    new_order.append(new_value)
            else:
                new_order.append(str(int(x) * 2024))
        counter -= 1
        input = new_order

    res = len(input)
    print(res)


if __name__ == "__main__":
    main()
