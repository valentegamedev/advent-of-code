input_data = []

def read_input_data():
    f = open("input/data.txt", "r")
    for i in f:
        data_items = i.split(",")
        for item in data_items:
            input_data.append(item)


def is_valid_id(id):
    for i in range(1, len(id)):
        left = id[:i]
        right = id[i:]
        if len(left) == len(right) and left == right:
            return False
    return True

#12599655151
def do_part_1():
    invalid_ids_sum = 0
    for id_range in input_data:
        ids = id_range.split("-")
        start = int(ids[0])
        end = int(ids[1])
        for i in range(start, end):
            if not is_valid_id(str(i)):
                invalid_ids_sum += i
    print(invalid_ids_sum)

def is_valid_2(id):
    #print(id)
    for i in range(0, len(id)):
        for j in range(i+1, len(id)+1):
            v = id[i:j]
            occurences_of_v = id.count(v)
            #print(v, occurences_of_v)
            if occurences_of_v >= 2:
                size_of_v = len(v)
                #print("yes", v, "->", size_of_v * occurences_of_v, len(id))
                if size_of_v * occurences_of_v == len(id):
                    return False
                pass
    return True

#20942028255
def do_part_2():
    invalid_ids_sum = 0
    for id_range in input_data:
        ids = id_range.split("-")
        start = int(ids[0])
        end = int(ids[1])
        for i in range(start, end):
            if not is_valid_2(str(i)):
                invalid_ids_sum += i
    print(invalid_ids_sum)

if __name__ == '__main__':
    read_input_data()
    #print(is_valid_2("1010"))
    #do_part_1()
    do_part_2()