from input import get_input_data_as_list, get_input_data_as_string


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    def get_num(x):
        i = 0
        while x[i].isdigit():
            i += 1
        if i > 3:
            return x[i:], -1
        return x[0:i], i

    def check_mul(s):
        x, i  = get_num(s)
        if i <= 0: return 0, i
        if s[i] != ',': return 0, i
        y, j = get_num(s[i+1:])
        if j <= 0: return 0, i+j
        if s[i+j+1] != ')': return 0, i+j
        return int(x)*int(y), i+j+2

    input = input_data_list
    res = 0 
    for xx in input:
        i = xx.find("mul(")
        s = xx[i+4:]
        while i != -1:
            r, new_index = check_mul(s)
            if r != 0:
                s = s[new_index:]
            res += r
            i = s.find("mul(")
            s = s[i+4:]

    print(res)


if __name__ == "__main__":
    main()
