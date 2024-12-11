from input import get_input_data_as_list, get_input_data_as_string


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_list

    list0 = [x.split("   ")[0] for x in input]
    list1 = [x.split("   ")[1] for x in input]
    list0.sort()
    list1.sort()
    res = 0
    for i in range(len(list0)):
        res += abs(int(list0[i]) - int(list1[i]))

    print(res)


if __name__ == "__main__":
    main()
