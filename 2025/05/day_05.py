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

#567
def do_part_1():
    set_of_fresh_ids = set()
    for range in fresh_range:
        for value in input_data:
            if range[0] <= value <= range[1]:
                set_of_fresh_ids.add(value)

    return len(set_of_fresh_ids)

#354149806372909
def do_part_2():
    global fresh_range

    final_fresh_range = []
    fresh_range = sorted(fresh_range, key=lambda v: v[0])
    #print(fresh_range)

    current_range = fresh_range[0]

    for range in fresh_range:
        if range[0] <= current_range[1]:
            current_range = (current_range[0], max(range[1], current_range[1]))
        else:
            final_fresh_range.append(current_range)
            current_range = range

    final_fresh_range.append(current_range)

    sum_ranges = 0
    for range in final_fresh_range:
        sum_ranges += range[1]-range[0]+1

    return sum_ranges

if __name__ == '__main__':
    read_input_data()
    #print(do_part_1())
    print(do_part_2())