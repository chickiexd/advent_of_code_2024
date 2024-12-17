from input import get_input_data_as_list, get_input_data_as_string


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_list
    input = [[int(y) for y in x] for x in input]

    directions = {
        0: (0, -1),
        1: (1, 0),
        2: (0, 1),
        3: (-1, 0),
    }

    def move(x, d):
        return (x[0] + d[0], x[1] + d[1])

    def get_trailheads(input):
        trailheads = []
        for y in range(len(input)):
            for x in range(len(input[0])):
                if input[y][x] == 0:
                    trailheads.append((x, y))
        return trailheads

    def in_bounds(p, x_len, y_len):
        if 0 <= p[0] < x_len and 0 <= p[1] < y_len:
            return 1
        return 0

    def find_path(input, crnt_loc, looking_for, results):
        if not in_bounds(crnt_loc, len(input[0]), len(input)):
            return 0
        if input[crnt_loc[1]][crnt_loc[0]] == 9 and looking_for == 9:
            if crnt_loc not in results:
                results.append(crnt_loc)
        elif input[crnt_loc[1]][crnt_loc[0]] == looking_for:
            for d in directions.keys():
                find_path(
                    input, move(crnt_loc, directions[d]), looking_for + 1, results
                )
        else:
            return 0

    trailheads = get_trailheads(input)
    res = 0
    for t in trailheads:
        results = []
        find_path(input, t, 0, results)
        res += len(results)

    print(res)


if __name__ == "__main__":
    main()
