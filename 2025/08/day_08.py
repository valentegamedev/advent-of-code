from scipy.spatial import distance
from itertools import combinations
import igraph as ig
import matplotlib.pyplot as plt

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
        input_data.append(tuple(junction_box)) #(ID, X, Y, Z)

    for i, j in combinations(input_data, 2):
        edges.append((i[0], j[0]))

    edges.sort(key=lambda edge: dist(edge[0], edge[1]))

def build_graph():
    global edges
    n = len(input_data)

    g = ig.Graph(n=n, directed=False)
    g.vs["value"] = input_data

    return g

def plot_igraph_3d(g, layout_3d):
    xs, ys, zs = map(list, zip(*layout_3d))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs, ys, zs, s=5)

    for e in g.es:
        s, t = e.tuple
        ax.plot([xs[s], xs[t]], [ys[s], ys[t]], [zs[s], zs[t]], linewidth=1)
    plt.show()

#66912
def do_part_1():
    g = build_graph()
    g.add_edges(edges[:1000])

    subgraphs = g.connected_components()
    sizes = sorted(subgraphs.sizes(), reverse=True)

    if len(sizes) < 3:
        print("Not enough subgraphs")
        return -1
    else:
        layout_3d = [(v["value"][1], v["value"][2], v["value"][3]) for v in g.vs]
        plot_igraph_3d(g, layout_3d)
        return sizes[0] * sizes[1] * sizes[2]



#724454082
def do_part_2():
    g = build_graph()

    for idx in range(0, len(edges)):
        if idx >= len(edges):
            break
        edge = edges[idx]
        g.add_edges([edge])

        order, _, _ = g.bfs(
            vid=edges[0][0],
        )

        if len(order) == len(input_data):
            layout_3d = [(v["value"][1], v["value"][2], v["value"][3]) for v in g.vs]
            plot_igraph_3d(g, layout_3d)
            return input_data[edge[0]][1] * input_data[edge[1]][1]

    return -1

if __name__ == '__main__':
    read_input_data()
    print(do_part_1())
    #print(do_part_2())