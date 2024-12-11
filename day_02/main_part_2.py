from input import get_input_data_as_list, get_input_data_as_string


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    def check_list(x, dampener):
        i = 0
        e = len(x)-1
        while i < e:
            if x[i] < x[i + 1] and 1 <= x[i + 1] - x[i] <= 3:
                i += 1
            else:
                if dampener:
                    return check_list(x[:i]+x[i+1:], False) or check_list(x[:i+1]+x[i+2:], False)
                else:
                    return False
        return True

    input = input_data_list
    input_as_list = [[int(y) for y in x.split(" ")] for x in input]
    safe = 0
    for x in input_as_list:
        if check_list(x, True) or check_list(x[::-1], True):
            safe += 1

    print(safe)

if __name__ == "__main__":
    main()
