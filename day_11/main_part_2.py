from collections import Counter
from input import get_input_data_as_list, get_input_data_as_string


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_list
    input = input[0].split(" ")

    c = Counter(input)

    counter = 75
    while counter > 0:
        iter = c.copy()
        for k in iter.keys():
            if iter[k] > 0:
                if k == "0":
                    c.update({"1": iter[k]})
                elif len(k) % 2 == 0:
                    new_value = k[: int(len(k) / 2)].lstrip("0")
                    if new_value == "":
                        c.update({"0": iter[k]})
                    else:
                        c.update({new_value: iter[k]})
                    new_value = k[int(len(k) / 2) :].lstrip("0")
                    if new_value == "":
                        c.update({"0": iter[k]})
                    else:
                        c.update({new_value: iter[k]})
                else:
                    c.update({str(int(k) * 2024): iter[k]})
                c[k] = c[k] - iter[k]
        counter -= 1

    print(c.total())


if __name__ == "__main__":
    main()
