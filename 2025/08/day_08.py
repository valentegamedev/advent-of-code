from scipy.spatial import distance
from itertools import combinations
import igraph as ig

input_data = []
edges = []

def dist(a, b):
    vertex_a = input_data[a]
    vertex_b = input_data[b]
    return distance.euclidean((vertex_a[1], vertex_a[2], vertex_a[3]), (vertex_b[1], vertex_b[2], vertex_b[3]))

def read_input_data():
    global edges
    f = open("input/data.txt", "r")
    for idx, i in enumerate(f):
        junction_box_string = i.strip().replace('\r', '').replace('\n', '').split(',')
        junction_box_string.insert(0, str(idx))
        junction_box = list(map(int, junction_box_string))
        input_data.append(tuple(junction_box))

    for i, j in combinations(input_data, 2):
        edges.append((i[0], j[0]))

    edges.sort(key=lambda edge: dist(edge[0], edge[1]))

    #print(edges)

def do_part_1():
    global edges
    n = len(input_data)

    g = ig.Graph(n=n, directed=False)
    g.vs["value"] = input_data

    g.add_edges(edges[:1000])

    subgraphs = g.connected_components()
    sizes = sorted(subgraphs.sizes(), reverse=True)

    if len(sizes) < 3:
        print("Not enough subgraphs")
        return -1
    else:
        return sizes[0] * sizes[1] * sizes[2]

def do_part_2():
    pass

if __name__ == '__main__':
    read_input_data()
    print(do_part_1())
    #do_part_2()