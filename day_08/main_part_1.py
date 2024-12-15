from input import get_input_data_as_list, get_input_data_as_string
import itertools


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_list
    input = [list(x) for x in input]

    def get_antinodes(p1, p2):
        a1 = (p1[0] + (p1[0] - p2[0]), p1[1] + (p1[1] - p2[1]))
        a2 = (p2[0] + (p2[0] - p1[0]), p2[1] + (p2[1] - p1[1]))
        return [a1, a2]

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
            found_antinodes = get_antinodes(p1, p2)
            found_antinodes = [
                x for x in found_antinodes if 0 <= x[0] < x_len and 0 <= x[1] < y_len
            ]
            for f in found_antinodes:
                if not f in antinodes:
                    antinodes.append(f)

    print(len(antinodes))


if __name__ == "__main__":
    main()
