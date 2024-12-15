from input import get_input_data_as_list, get_input_data_as_string
import itertools


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_list
    input = [list(x) for x in input]

    def minus(p, vector):
        return (p[0] - vector[0], p[1] - vector[1])

    def plus(p, vector):
        return (p[0] + vector[0], p[1] + vector[1])

    def in_bounds(p, x_len, y_len):
        if 0 <= p[0] < x_len and 0 <= p[1] < y_len:
            return 1
        return 0

    def get_antinodes(p1, p2, x_len, y_len):
        a1_vector = (p1[0] - p2[0], p1[1] - p2[1])
        a2_vector = (p2[0] - p1[0], p2[1] - p1[1])
        antinodes = []
        p1_plus = plus(p1, a1_vector)
        p1_minus = minus(p1, a1_vector)
        p2_plus = plus(p2, a2_vector)
        p2_minus = minus(p2, a2_vector)

        while in_bounds(p1_plus, x_len, y_len):
            if not p1_plus in antinodes:
                antinodes.append(p1_plus)
            p1_plus = plus(p1_plus, a1_vector)

        while in_bounds(p1_minus, x_len, y_len):
            if not p1_minus in antinodes:
                antinodes.append(p1_minus)
            p1_minus = minus(p1_minus, a1_vector)

        while in_bounds(p2_plus, x_len, y_len):
            if not p2_plus in antinodes:
                antinodes.append(p2_plus)
            p2_plus = plus(p2_plus, a2_vector)

        while in_bounds(p2_minus, x_len, y_len):
            if not p2_minus in antinodes:
                antinodes.append(p2_minus)
            p2_minus = minus(p2_minus, a2_vector)
        return antinodes

    x_len = len(input[0])
    y_len = len(input)

    frequencies = {}
    for i, y in enumerate(input):
        for j, x in enumerate(y):
            if x != ".":
                if not x in frequencies.keys():
                    frequencies[x] = []
                frequencies[x].append((j, i))

    antinodes = []
    for k in frequencies.keys():
        combinations = list(itertools.combinations(frequencies[k], 2))
        for c in combinations:
            p1 = c[0]
            p2 = c[1]
            found_antinodes = get_antinodes(p1, p2, x_len, y_len)
            for f in found_antinodes:
                if not f in antinodes:
                    antinodes.append(f)

    print(len(antinodes))


if __name__ == "__main__":
    main()
