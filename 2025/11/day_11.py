import igraph as ig
from functools import lru_cache

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

#566
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

#331837854931968
def do_part_2():
    svr_idx = nodes.index('svr')
    fft_idx = nodes.index('fft')
    dac_idx = nodes.index('dac')
    out_idx = nodes.index('out')

    n = len(nodes)
    node_to_idx = {name: i for i, name in enumerate(nodes)}

    g = ig.Graph(n=n, directed=True)
    g.add_edges([(node_to_idx[a], node_to_idx[b]) for a, b in edges])

    reachable_from_fft = set(g.subcomponent(fft_idx, mode='OUT'))
    can_reach_dac = set(g.subcomponent(dac_idx, mode='IN'))
    fft_dac_intersection = reachable_from_fft & can_reach_dac

    pruned_graph = {
        fft_idx: set(g.subcomponent(fft_idx, mode="IN")),
        dac_idx: fft_dac_intersection,
        out_idx: set(g.subcomponent(out_idx, mode="IN"))
    }

    @lru_cache(maxsize=None)
    def dfs(u, t, visited_frozenset):

        # base case
        if u == t:
            return 1

        visited = set(visited_frozenset)
        total = 0

        for v in g.neighbors(u, mode='OUT'):
            if v in visited:
                continue

            if v not in pruned_graph[t]:
                continue

            total += dfs(v, t, frozenset(visited | {v}))

        return total

    svr_fft = dfs(svr_idx, fft_idx, frozenset({svr_idx})) #7329
    print(svr_fft)
    dfs.cache_clear()
    fft_dac = dfs(fft_idx, dac_idx, frozenset({fft_idx})) #8039306
    print(fft_dac)
    dfs.cache_clear()
    dac_out = dfs(dac_idx, out_idx, frozenset({dac_idx})) #5632
    print(dac_out)
    dfs.cache_clear()

    result = svr_fft * fft_dac * dac_out

    return result


if __name__ == '__main__':
    read_input_data()
    #print(do_part_1())
    print(do_part_2())