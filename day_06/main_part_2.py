from input import get_input_data_as_list, get_input_data_as_string


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    directions = {
        0: (0, -1),
        1: (1, 0),
        2: (0, 1),
        3: (-1, 0),
    }

    input = input_data_list

    input = [list(x) for x in input]

    direction = 0

    for x in range(len(input[0])):
        for y in range(len(input)):
            if input[y][x] == "^":
                start = (x, y)
                input[y][x] = "|"
                break

    def check(maze, x, y, direction, seen):
        d = directions[direction]
        new_x = x + d[0]
        new_y = y + d[1]
        while 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze):
            if maze[new_y][new_x] == "#":
                if (x, y, direction) in seen:
                    # print(seen)
                    return 1
                else:
                    new_direction = (direction + 1) % 4
                    seen.append((x, y, direction))
                    # print(seen)
                    return check(maze, x, y, new_direction, seen)
            x = new_x
            y = new_y
            new_x += d[0]
            new_y += d[1]
        return 0

    def move(maze, x, y, direction, start):
        counter = 0
        d = directions[direction]
        new_x = x + d[0]
        new_y = y + d[1]
        while 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze):
            if maze[new_y][new_x] == "#":
                direction = (direction + 1) % 4
                maze[y][x] = "+"
                return counter + move(maze, x, y, direction, start)
            else:
                if (new_x, new_y) != start and maze[new_y][new_x] == ".":
                    direction_to_check = (direction + 1) % 4
                    temp = maze[new_y][new_x]
                    maze[new_y][new_x] = "#"
                    c = check(maze, x, y, direction_to_check, [])
                    maze[new_y][new_x] = temp
                    counter += c
                if direction == 0 or direction == 2:
                    if maze[new_y][new_x] == "-" or maze[new_y][new_x] == "+":
                        maze[new_y][new_x] = "+"
                    else:
                        maze[new_y][new_x] = "|"
                if direction == 1 or direction == 3:
                    if maze[new_y][new_x] == "|" or maze[new_y][new_x] == "+":
                        maze[new_y][new_x] = "+"
                    else:
                        maze[new_y][new_x] = "-"
                x = new_x
                y = new_y
                new_x += d[0]
                new_y += d[1]
        return counter

    counter = move(input, start[0], start[1], direction, start)

    print(counter)


if __name__ == "__main__":
    main()
