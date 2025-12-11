import igraph as ig
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

def draw_graph_interactive(g: ig.Graph,
                           node_labels=None,
                           highlight_paths=None,
                           figsize=(8, 5),
                           node_size=25,
                           node_color='tab:blue',
                           node_label_size=10,
                           edge_width=1.0,
                           arrow_size=12):
    # labels
    if node_labels is None:
        if "value" in g.vs.attribute_names():
            node_labels = g.vs["value"]
        else:
            node_labels = [str(i) for i in range(len(g.vs))]

    try:
        layout = g.layout("fr")
    except Exception:
        layout = g.layout("circle")

    coords = layout.coords
    xs = [c[0] for c in coords]
    ys = [c[1] for c in coords]

    # normalize coordinates to nicer plotting range
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)
    dx = maxx - minx if maxx != minx else 1.0
    dy = maxy - miny if maxy != miny else 1.0
    margin = 0.08
    max_span = max(dx, dy)
    xs = [(x - minx) / max_span for x in xs]
    ys = [(y - miny) / max_span for y in ys]

    fig, ax = plt.subplots(figsize=figsize)
    ax.set_aspect('equal')
    ax.axis('off')

    # an arrowed edge between two points
    def draw_edge(x1, y1, x2, y2, color='gray', lw=edge_width, arrow=True, zorder=1):
        # shrink endpoints by a small amount (relative)
        def shrink(a, b, frac=0.06):
            dx = b[0]-a[0]
            dy = b[1]-a[1]
            return (a[0] + dx*frac, a[1] + dy*frac), (b[0] - dx*frac, b[1] - dy*frac)

        (sx, sy), (ex, ey) = shrink((x1, y1), (x2, y2), frac=0.07)
        if g.is_directed() and arrow:
            arr = FancyArrowPatch((sx, sy), (ex, ey),
                                  arrowstyle='-|>', mutation_scale=arrow_size,
                                  linewidth=lw, zorder=zorder, color=color)
            ax.add_patch(arr)
        else:
            ax.plot([sx, ex], [sy, ey], linewidth=lw, zorder=zorder, color=color)

    # draw all edges
    for e in g.es:
        src = e.tuple[0]
        dst = e.tuple[1]
        draw_edge(xs[src], ys[src], xs[dst], ys[dst], color='black', lw=edge_width, arrow=True, zorder=1)

    # draw highlighted paths (if any)
    if highlight_paths:
        colors = ['crimson', 'tab:orange', 'tab:green', 'tab:purple', 'tab:brown']
        for pi, path in enumerate(highlight_paths):
            col = colors[pi % len(colors)]
            # draw path edges thicker and colored
            for a, b in zip(path[:-1], path[1:]):
                draw_edge(xs[a], ys[a], xs[b], ys[b], color=col, lw=edge_width*2.2, arrow=True, zorder=2)

            # draw nodes on the path with a ring
            ax.scatter([xs[i] for i in path], [ys[i] for i in path],
                       s=node_size*1.4, facecolors='none', edgecolors=col, linewidths=2.0, zorder=4)

    # draw nodes
    ax.scatter(xs, ys, s=node_size, zorder=3, edgecolors='k', linewidths=0.6, facecolors=node_color)

    #good = ['svr', 'fft', 'dac', 'out']
    # draw labels
    for i, label in enumerate(node_labels):
        #new_label = label if label in good else ''
        ax.text(xs[i], ys[i], str(label), fontsize=node_label_size,
                ha='center', va='center', zorder=5,
                bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none', alpha=0.8))

    # auto scale margins
    ax.set_xlim(-margin, 1 + margin)
    ax.set_ylim(-margin, 1 + margin)

    plt.title("Graph visualization (pan/zoom enabled)")
    plt.show(block=True)  # interactive window