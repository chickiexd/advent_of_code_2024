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
                input[y][x] = "x"
                break


    def move(maze, x, y, direction):
        d = directions[direction]
        new_x = x + d[0]
        new_y = y + d[1]
        while 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze):
            if maze[new_y][new_x] == "#":
                direction = (direction + 1) % 4
                return move(maze, x, y, direction)
            else:
                maze[new_y][new_x] = "x"
                x = new_x
                y = new_y
                new_x += d[0]
                new_y += d[1]
        return 0

    move(input, start[0], start[1], direction)

    counter = 0
    for x in input:
        for y in x:
            if y == "x":
                counter += 1

    # with open("output.txt", "w") as file:
    #     for x in input:
    #         file.write(f"{"".join(x)}\n")

    print(counter)



if __name__ == "__main__":
    main()
