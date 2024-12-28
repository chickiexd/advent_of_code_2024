from input import get_input_data_as_list, get_input_data_as_string
import copy


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_string

    def move(x, d):
        return (x[0] + d[0], x[1] + d[1])

    def get_pos(maze, point):
        return maze[point[1]][point[0]]

    def set_pos(maze, point, char):
        maze[point[1]][point[0]] = char

    maze = input.split("\n\n")[0]
    moves = input.split("\n\n")[1]
    maze = maze.split("\n")
    maze = [list(x) for x in maze]
    moves = moves.replace("\n", "")

    expanded_maze = []
    for y in range(len(maze)):
        expanded_maze.append([])
        for x in range(len(maze[0])):
            if get_pos(maze, (x, y)) == "#":
                expanded_maze[y].append("#")
                expanded_maze[y].append("#")
            if get_pos(maze, (x, y)) == ".":
                expanded_maze[y].append(".")
                expanded_maze[y].append(".")
            if get_pos(maze, (x, y)) == "O":
                expanded_maze[y].append("[")
                expanded_maze[y].append("]")
            if get_pos(maze, (x, y)) == "@":
                expanded_maze[y].append("@")
                expanded_maze[y].append(".")

    maze = expanded_maze

    directions = {
        "<": (-1, 0),
        ">": (+1, 0),
        "v": (0, +1),
        "^": (0, -1),
    }

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
        if d == "<" or d == ">":
            while True:
                crnt_position = move(crnt_position, directions[d])
                if get_pos(maze, crnt_position) == "#":
                    go = False
                    break
                elif get_pos(maze, crnt_position) == ".":
                    break
                elif (
                    get_pos(maze, crnt_position) == "["
                    or get_pos(maze, crnt_position) == "]"
                ):
                    boxes.append(crnt_position)
        else:
            new_positions = [crnt_position]
            while True:
                break_count = 0
                crnt_positions = [move(p, directions[d]) for p in new_positions]
                new_positions = []
                for crnt_position in crnt_positions:
                    if get_pos(maze, crnt_position) == "#":
                        go = False
                    elif get_pos(maze, crnt_position) == ".":
                        break_count += 1
                    elif get_pos(maze, crnt_position) == "[":
                        new_positions.append(crnt_position)
                        new_positions.append(move(crnt_position, directions[">"]))
                    elif get_pos(maze, crnt_position) == "]":
                        new_positions.append(crnt_position)
                        new_positions.append(move(crnt_position, directions["<"]))
                boxes.extend(new_positions)
                if not go:
                    break
                elif break_count == len(crnt_positions):
                    break

        if go:
            saved_state = copy.deepcopy(maze)
            set_pos(maze, boxes[0], ".")
            new_robot_pos = move(boxes[0], directions[d])
            set_pos(maze, new_robot_pos, "@")
            for b in boxes[1:]:
                move_to = move(b, directions[d])
                set_pos(maze, move_to, get_pos(saved_state, b))
                prev_point = False
                if d == "^":
                    prev_point = move(b, directions["v"])
                elif d == "v":
                    prev_point = move(b, directions["^"])
                if prev_point:
                    if prev_point not in boxes:
                        set_pos(maze, b, ".")
            crnt_position = new_robot_pos
        else:
            crnt_position = boxes[0]

    res = 0
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if get_pos(maze, (x, y)) == "[":
                res += 100 * y + x

    print(res)


if __name__ == "__main__":
    main()
