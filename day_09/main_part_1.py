from input import get_input_data_as_list, get_input_data_as_string


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_string
    input = input.replace("/n", "")
    input = input[:-1]

    disk = []

    for i, c in enumerate(input):
        for _ in range(int(c)):
            if i % 2 == 0:
                disk.append(int(i / 2))
            else:
                disk.append(".")

    for i in range(1, len(disk)):
        if i == 0 or i == 1 or "." in disk[:-i]:
            j = disk.index(".")
            disk[j], disk[-i] = disk[-i], disk[j]
        else:
            break

    res = 0
    for i, n in enumerate(disk):
        if n != ".":
            res += i * n
        else:
            break

    print(res)


if __name__ == "__main__":
    main()
