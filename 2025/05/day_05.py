fresh_range = []
input_data = []

def read_input_data():
    f = open("input/data.txt", "r")
    reading_range = True
    for i in f:
        row = i.strip().replace('\r', '').replace('\n', '')
        if row == '':
            reading_range = False
            continue

        if reading_range:
            row_split = i.split('-')
            range_tuple = (int(row_split[0]), int(row_split[1]))
            fresh_range.append(range_tuple)
        else:
            input_data.append(int(row))

def do_part_1():
    set_of_fresh_ids = set()
    for range in fresh_range:
        for value in input_data:
            if range[0] <= value <= range[1]:
                set_of_fresh_ids.add(value)

    return len(set_of_fresh_ids)

def do_part_2():
    pass

if __name__ == '__main__':
    read_input_data()
    print(do_part_1())
    #do_part_2()