from collections import Counter
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
    seconds = 10000

    def move(p, v, s):
        end_point = ((p[0] + v[0] * s) % x_len, (p[1] + v[1] * s) % y_len)
        return end_point

    def write_grid(points,file_path):
        max_x = max(p[0] for p in points)
        max_y = max(p[1] for p in points)
        grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        for x, y in points:
            grid[y][x] = 'X'
        with open(file_path, "w") as file:
            for x in grid:
                file.write("".join(x))
                file.write("\n")

    maxis = []
    max_unique = 0
    for x in range(seconds):
        positions = []
        for r in robots:
            ending_at = move(r[0], r[1], x)
            positions.append(ending_at)
        c = Counter(positions)
        t = sum(count in {1} for count in c.values())
        if t > max_unique:
            maxis.append((t, x))
            max_unique = t
            write_grid(positions, f"grid_{x}.txt")
    print(maxis)


if __name__ == "__main__":
    main()
