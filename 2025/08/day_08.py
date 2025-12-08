from scipy.spatial import distance
from itertools import combinations

input_data = []
edges = []

def dist(a, b):
    return distance.euclidean(a, b)

def read_input_data():
    global edges
    f = open("input/data.txt", "r")
    for i in f:
        junction_box_string = i.strip().replace('\r', '').replace('\n', '').split(',')
        junction_box = list(map(int, junction_box_string))
        input_data.append(tuple(junction_box))

    for i, j in combinations(input_data, 2):
        edges.append((i, j))

    edges.sort(key=lambda edge: dist(edge[0], edge[1]))

def do_part_1():
    print(edges)

def do_part_2():
    pass

if __name__ == '__main__':
    read_input_data()
    do_part_1()
    #do_part_2()