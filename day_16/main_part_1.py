from input import get_input_data_as_list, get_input_data_as_string
from queue import PriorityQueue


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_list
    input = [list(x) for x in input]

    directions = {
        0: (0, -1),
        1: (1, 0),
        2: (0, 1),
        3: (-1, 0),
    }

    def get_pos(maze, char):
        for y in range(len(maze)):
            for x in range(len(maze[0])):
                if maze[y][x] == char:
                    return (x, y)

    def get_char(maze, p):
        return maze[p[1]][p[0]]

    def move(x, d):
        return (x[0] + d[0], x[1] + d[1])

    start = get_pos(input, "S")
    end = get_pos(input, "E")

    q = PriorityQueue()
    q.put((0, start, 1))

    res = 0
    seen = set()
    while not q.empty():
        crnt = q.get()
        seen.add(crnt[1])
        if crnt[1] == end:
            res = crnt[0]
            break
        for d in directions:
            next_point = move(crnt[1], directions[d])
            if next_point in seen:
                continue
            if get_char(input, next_point) == "." or get_char(input, next_point) == "E":
                prev_moving_direction = crnt[2]
                if prev_moving_direction == d:
                    q.put((crnt[0] + 1, next_point, d))
                elif (
                    prev_moving_direction == (d - 1) % 4
                    or prev_moving_direction == (d + 1) % 4
                ):
                    q.put((crnt[0] + 1001, next_point, d))

    print(res)


if __name__ == "__main__":
    main()
