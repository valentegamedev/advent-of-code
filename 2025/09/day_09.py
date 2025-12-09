from itertools import combinations

input_data = []

def read_input_data():
    f = open("input/data.txt", "r")
    for i in f:
        tiles_string = i.strip().replace('\r', '').replace('\n', '').split(',')
        input_data.append((int(tiles_string[0]), int(tiles_string[1])))
    print(input_data)

#4749929916
def do_part_1():
    biggest_area = 0
    for i, j in combinations(input_data, 2):
        x1, y1 = i
        x2, y2 = j
        w = abs(x2 - x1)
        h = abs(y2 - y1)
        area = (w + 1) * (h + 1)
        if area > biggest_area:
            biggest_area = area

    return biggest_area

def do_part_2():
    pass

if __name__ == '__main__':
    read_input_data()
    print(do_part_1())
    #do_part_2()