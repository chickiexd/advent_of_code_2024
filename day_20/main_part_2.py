from input import get_input_data_as_list, get_input_data_as_string
from queue import PriorityQueue
from collections import Counter


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_list
    input = [list(x) for x in input]
    maze_size = len(input)

    directions = {
        0: (0, -1),
        1: (1, 0),
        2: (0, 1),
        3: (-1, 0),
    }

    def find_char(maze, char):
        for y in range(len(maze)):
            for x in range(len(maze[0])):
                if maze[y][x] == char:
                    return (x, y)

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

    start = find_char(input, "S")
    end = find_char(input, "E")

    def create_maze(maze):
        q = PriorityQueue()
        # score, point, direction
        q.put((0, start, None))
        seen = set()
        while not q.empty():
            s, p, _d = q.get()
            if (p, _d) in seen:
                continue
            seen.add((p, _d))
            if isinstance(get_char(maze, p), str) or get_char(maze, p) >= s:
                set_char(maze, p, s)
            if p == end:
                pass
            for d in directions:
                next_point = move(p, directions[d])
                if not in_bounds(next_point):
                    continue
                if (next_point, d) in seen:
                    continue
                if get_char(maze, next_point) == "#":
                    continue
                q.put((s + 1, next_point, d))

    def h(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    maze = input
    create_maze(maze)
    path = [
        (x, y)
        for x in range(len(maze))
        for y in range(len(maze))
        if isinstance(get_char(maze, (x, y)), int)
    ]
    shortcuts = []
    seen = set()
    for p1 in path:
        for p2 in path:
            l = [p1, p2]
            l.sort()
            if tuple(l) in seen:
                continue
            if h(p1, p2) <= 20:
                timesave = abs(get_char(maze, p1) - get_char(maze, p2)) - h(p1, p2)
                if timesave >= 100:
                    seen.add(tuple(l))
                    shortcuts.append((tuple(l), timesave))

    print(len(shortcuts))


if __name__ == "__main__":
    main()
