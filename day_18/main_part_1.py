from input import get_input_data_as_list, get_input_data_as_string
from queue import PriorityQueue


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_list
    input = [tuple(x.split(",")) for x in input]
    input = [(int(x), int(y)) for x, y in input]
    maze_size = 71

    directions = {
        0: (0, -1),
        1: (1, 0),
        2: (0, 1),
        3: (-1, 0),
    }

    def get_char(maze, p):
        return maze[p[1]][p[0]]

    def set_char(maze, p, char):
        maze[p[1]][p[0]] = char

    def move(x, d):
        return (x[0] + d[0], x[1] + d[1])

    def in_bounds(p):
        if 0 <= p[0] < maze_size and 0 <= p[1] < maze_size:
            return 1
        return 0

    def h(p):
        return abs(p[0] - (maze_size - 1)) + abs(p[1] - (maze_size - 1))

    start = (0, 0)
    end = (maze_size - 1, maze_size - 1)

    def generate_maze(size, corrupted_length):
        maze = [["." for x in range(size)] for y in range(size)]
        for i in range(corrupted_length):
            set_char(maze, input[i], "#")
        return maze

    def get_path(maze):
        q = PriorityQueue()
        # priority, score, position
        q.put((h(start), 0, start))
        seen = set()
        while not q.empty():
            _, s, p = q.get()
            if p in seen:
                continue
            seen.add(p)
            if p == end:
                print(s)
                return s
            for d in directions:
                next_point = move(p, directions[d])
                if not in_bounds(next_point):
                    continue
                if get_char(maze, next_point) == "#":
                    continue
                if next_point in seen:
                    continue
                q.put((s + h(next_point), s + 1, next_point))

    maze = generate_maze(maze_size, 1024)
    res = get_path(maze)
    print(res)


if __name__ == "__main__":
    main()
