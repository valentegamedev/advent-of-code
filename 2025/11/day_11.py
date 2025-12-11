import igraph as ig

input_data = []
nodes = []
edges = []

def read_input_data():
    global nodes, edges
    f = open("input/data.txt", "r")
    all_nodes = set()
    for i in f:
        row = i.strip().replace('\r', '').replace('\n', '')
        all_nodes_in_row = row.replace(':', '').split(' ')
        all_nodes.update(all_nodes_in_row)
        input_data.append(i.strip().replace('\r', '').replace('\n', ''))
        node_connection_split = row.split(':')
        node = node_connection_split[0]
        connections = node_connection_split[1][1:].split(' ')
        for c in connections:
            edges.append((node, c))
    nodes = list(all_nodes)

    #print(edges)
    #print(nodes)

def do_part_1():
    #print(nodes)
    you_idx = nodes.index('you')
    out_idx = nodes.index('out')

    n = len(nodes)

    g = ig.Graph(n=n, directed=True)
    g.vs["value"] = nodes

    nodes_to_idx_dic = {s: i for i, s in enumerate(nodes)}

    edges_with_idxs = []
    for edge in edges:
        edges_with_idxs.append((nodes_to_idx_dic[edge[0]], nodes_to_idx_dic[edge[1]]))

    g.add_edges(edges_with_idxs)

    print(g)

    paths = g.get_all_simple_paths(v=you_idx, to=out_idx, mode='OUT')

    return len(paths)

def do_part_2():
    pass

if __name__ == '__main__':
    read_input_data()
    print(do_part_1())
    #do_part_2()