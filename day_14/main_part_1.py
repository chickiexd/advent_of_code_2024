from input import get_input_data_as_list, get_input_data_as_string


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_list

    robots = [x.split(" ") for x in input]
    robots = [
        (tuple(p.lstrip("p=").split(",")), tuple(v.lstrip("v=").split(",")))
        for p, v in robots
    ]
    robots = [([int(p) for p in pp], [int(v) for v in vv]) for pp, vv in robots]

    y_len = 103
    x_len = 101
    seconds = 100

    def move(p, v, s):
        end_point = ((p[0] + v[0] * s) % x_len, (p[1] + v[1] * s) % y_len)
        return end_point

    q1, q2, q3, q4 = 0, 0, 0, 0
    for r in robots:
        ending_at = move(r[0], r[1], seconds)
        if ending_at[0] < int(x_len / 2) and ending_at[1] < int(y_len / 2):
            q1 += 1
        if ending_at[0] < int(x_len / 2) and ending_at[1] > int(y_len / 2):
            q2 += 1
        if ending_at[0] > int(x_len / 2) and ending_at[1] < int(y_len / 2):
            q3 += 1
        if ending_at[0] > int(x_len / 2) and ending_at[1] > int(y_len / 2):
            q4 += 1
    print(q1 * q2 * q3 * q4)


if __name__ == "__main__":
    main()
