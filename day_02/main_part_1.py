from input import get_input_data_as_list, get_input_data_as_string


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_list

    input_as_list = [[int(y) for y in x.split(" ")] for x in input]
    break_counter = 0
    for x in input_as_list:
        asc = True
        for i in range(len(x) - 1):
            if i == 0:
                if x[i] > x[i + 1]:
                    asc = False
            if asc and x[i] < x[i + 1] and 1 <= x[i + 1] - x[i] <= 3:
                pass
            elif not asc and x[i] > x[i + 1] and 1 <= x[i] - x[i + 1] <= 3:
                pass
            else:
                break_counter += 1
                break
    print(len(input_as_list) - break_counter)


if __name__ == "__main__":
    main()
