from input import get_input_data_as_list, get_input_data_as_string


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    global debug

    def check(s, x, y):
        looking_for = ["AMS", "ASM"]
        wanted = []
        wanted.append(s[x][y])
        wanted2 = wanted.copy()
        xx_1 = x - 1
        xx_2 = x + 1
        yy_1 = y - 1
        yy_2 = y + 1
        if 0 <= xx_1 < len(s) and 0 <= yy_1 < len(s[0]) and 0 <= yy_2 < len(s[0]) and 0 <= xx_2 < len(s):
            wanted.append(s[xx_1][yy_1])
            wanted.append(s[xx_2][yy_2])
            wanted2.append(s[xx_1][yy_2])
            wanted2.append(s[xx_2][yy_1])

        if "".join(wanted) in looking_for and "".join(wanted2) in looking_for:
            return 1
        return 0

    input = input_data_list
    results = []
    for x in range(len(input)):
        for y in range(len(input[x])):
            if input[x][y] == "A":
                results.append(check(input, x, y))

    print(sum(results))


if __name__ == "__main__":
    main()
