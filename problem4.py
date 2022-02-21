def missing_int(num_list):
    list_len = len(num_list)
    missing_pos_int = 1
    num_list.sort()
    for x in range(list_len):
        if num_list[x]+ 1 == list_len:
            missing_pos_int = num_list[x] + 1
            return missing_pos_int
        if num_list[x] < 1:
            continue
        else:
            if num_list[x] + 1 == num_list[x + 1]:
                continue
            else:
                missing_pos_int = num_list[x] + 1
                return missing_pos_int

    return missing_pos_int

if __name__ == '__main__':
#    num_list = [3, 4, -1, 1]
    num_list = [1, 2, 0]
    answer = missing_int(num_list)
    print(answer)