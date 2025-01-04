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

    def get_shortcuts(maze):
        def check_shortcut(maze, p):
            setup = [isinstance(get_char(maze, move(p, directions[d])), int) for d in directions if in_bounds(move(p, directions[d]))]
            if setup == [True, False, True, False]:
                return abs(get_char(maze, move(p, directions[0])) - get_char(maze, move(p, directions[2]))) 
            elif setup == [False, True, False, True]:
                return abs(get_char(maze, move(p, directions[1])) - get_char(maze, move(p, directions[3]))) 

        shortcuts = []
        for y in range(len(maze)):
            for x in range(len(maze)):
                if get_char(maze, (x, y)) == "#":
                    shorcut_l = check_shortcut(maze, (x, y))
                    if shorcut_l:
                        shortcuts.append(shorcut_l-2)
        return shortcuts


    maze = input
    create_maze(maze)
    shortcuts = get_shortcuts(maze)
    shortcuts.sort()
    s_count = Counter(shortcuts)

    res = 0
    for k, v in s_count.items():
        if k >= 100:
            res += v

    print(res)


if __name__ == "__main__":
    main()
