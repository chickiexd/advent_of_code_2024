from collections import Counter
from input import get_input_data_as_list, get_input_data_as_string


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_list

    list0 = [int(x.split("   ")[0]) for x in input]
    list1 = [int(x.split("   ")[1]) for x in input]
    list0.sort()
    list1.sort()
    res = 0
    counts0 = Counter(list0)
    counts1 = Counter(list1)
    for x in counts0.keys():
        res += x * counts1[x]
    print(res)


if __name__ == "__main__":
    main()
