from input import get_input_data_as_list, get_input_data_as_string


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_string

    maze = input.split("\n\n")[0]
    moves = input.split("\n\n")[1]
    maze = maze.split("\n")
    maze = [list(x) for x in maze]
    moves = moves.replace("\n", "")

    directions = {
        "<": (-1, 0),
        ">": (+1, 0),
        "v": (0, +1),
        "^": (0, -1),
    }

    def move(x, d):
        return (x[0] + d[0], x[1] + d[1])

    def get_pos(maze, point):
        return maze[point[1]][point[0]]

    def set_pos(maze, point, char):
        maze[point[1]][point[0]] = char

    robot_position = tuple()
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if get_pos(maze, (x, y)) == "@":
                robot_position = (x, y)
                break

    crnt_position = robot_position
    for d in moves:
        boxes = [crnt_position]
        go = True
        while True:
            crnt_position = move(crnt_position, directions[d])
            if get_pos(maze, crnt_position) == "#":
                go = False
                break
            elif get_pos(maze, crnt_position) == ".":
                break
            elif get_pos(maze, crnt_position) == "O":
                boxes.append(crnt_position)
        if go:
            set_pos(maze, boxes[0], ".")
            new_robot_pos = move(boxes[0], directions[d])
            set_pos(maze, new_robot_pos, "@")
            for b in boxes[1:]:
                moved_to = move(b, directions[d])
                set_pos(maze, moved_to, "O")
            crnt_position = new_robot_pos
        else:
            crnt_position = boxes[0]

    res = 0
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if get_pos(maze, (x, y)) == "O":
                res += 100 * y + x

    print(res)


if __name__ == "__main__":
    main()
