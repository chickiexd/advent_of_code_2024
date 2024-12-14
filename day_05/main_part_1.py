from input import get_input_data_as_list, get_input_data_as_string


def main():
    input_data_list = get_input_data_as_list()
    input_data_list_test = get_input_data_as_list(test=True)
    input_data_string = get_input_data_as_string()
    input_data_string_test = get_input_data_as_string(test=True)

    input = input_data_list
    ordering = []
    produce = []
    i = 0
    while input[i]:
        ordering.append(input[i])
        i += 1
    i += 1
    while i < len(input):
        produce.append(input[i])
        i += 1
    produce = [x.split(",") for x in produce]

    ordering_dict = {}
    for i in ordering:
        nums = i.split("|")
        if nums[0] not in ordering_dict.keys():
            ordering_dict[nums[0]] = [[], []]
        if nums[1] not in ordering_dict.keys():
            ordering_dict[nums[1]] = [[], []]
        ordering_dict[nums[0]][1].append(nums[1])
        ordering_dict[nums[1]][0].append(nums[0])


    valid_ps = []
    for p in produce:
        # nums = p.split(",")
        valid = True
        for i, c in enumerate(p):
            for x in p[i+1:]:
                if x in ordering_dict[c][0]:
                    valid = False
                    break
        if valid:
            valid_ps.append(p)

    res = 0
    for v in valid_ps:
        x = int(len(v)/2)
        res += int(v[x])

        
    print(res)




if __name__ == "__main__":
    main()
