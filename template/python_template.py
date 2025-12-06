input_data = []

def read_input_data():
    f = open("input/data.txt", "r")
    for i in f:
        input_data.append(i.strip().replace('\r', '').replace('\n', ''))

def do_part_1():
    print(input_data)

def do_part_2():
    pass

if __name__ == '__main__':
    read_input_data()
    do_part_1()
    #do_part_2()