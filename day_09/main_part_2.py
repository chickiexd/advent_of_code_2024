from input import get_input_data_as_list, get_input_data_as_string


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_string
    input = input.replace("/n", "")
    input = input[:-1]

    files = []
    spaces = []
    for i, x in enumerate(input):
        if not i % 2 == 0:
            spaces.append(int(x))
        else:
            # len, id, moveable
            files.append([int(x), int(i / 2), True])

    head = []

    def fill_space(head, files, space):
        j = 1
        while space > 0:
            if j >= len(files):
                break
            elif space >= files[-j][0] and files[-j][2]:
                head.extend([files[-j][1] for _ in range(files[-j][0])])
                space = space - files[-j][0]
                files[-j][2] = False
            else:
                j += 1
        if space > 0:
            head.extend(["." for _ in range(space)])

    i = 0
    while i < len(files):
        if files[i][2]:
            head.extend([files[i][1] for _ in range(files[i][0])])
        else:
            fill_space(head, files[i:], files[i][0])
        if i < len(spaces):
            fill_space(head, files[i:], spaces[i])
        i += 1

    res = 0
    for i, n in enumerate(head):
        if n != ".":
            res += i * n

    print(res)


if __name__ == "__main__":
    main()
