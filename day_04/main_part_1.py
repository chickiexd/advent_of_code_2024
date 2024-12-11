from input import get_input_data_as_list, get_input_data_as_string


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    global debug

    def check(s, x, y, direction):
        looking_for = "XMAS"
        wanted = []
        wanted.append(s[x][y])
        for i in range(1, len(looking_for)):
            xx = x + direction[0] * i
            yy = y + direction[1] * i
            if 0 <= xx < len(s[0]) and 0 <= yy < len(s):
                wanted.append(s[xx][yy])
        if looking_for == "".join(wanted):
            return 1
        return 0

    right = (1, 0)
    left = (-1, 0)
    up = (0, -1)
    down = (0, 1)
    up_right = (1, -1)
    up_left = (-1, -1)
    down_right = (1, 1)
    down_left = (-1, 1)

    input = input_data_list
    debug = [['.' for y in x] for x in input]
    results = []
    for x in range(len(input)):
        for y in range(len(input[x])):
            if input[x][y] == "X":
                results.append(check(input, x, y, right))
                results.append(check(input, x, y, left))
                results.append(check(input, x, y, up))
                results.append(check(input, x, y, down))
                results.append(check(input, x, y, up_right))
                results.append(check(input, x, y, up_left))
                results.append(check(input, x, y, down_right))
                results.append(check(input, x, y, down_left))

    print(sum(results))

if __name__ == "__main__":
    main()
