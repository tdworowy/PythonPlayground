import math

import networkx as nx
from itertools import permutations, chain, combinations


def dist(x1: int, y1: int, x2: int, y2: int) -> float:
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def get_graph(coordinates: list) -> nx.Graph:
    g = nx.Graph()
    n = len(coordinates)
    for i in range(n):
        for j in range(i + 1):
            g.add_edge(
                i,
                j,
                weight=dist(
                    coordinates[i][0],
                    coordinates[i][1],
                    coordinates[j][0],
                    coordinates[j][1],
                ),
            )
    return g


def cycle_length(g: nx.Graph, cycle: list) -> int:
    assert len(cycle) == g.number_of_nodes()
    weights = 0
    for i in range(len(cycle) - 1):
        weights += g[cycle[i]][cycle[i + 1]]["weight"]
    weights += g[cycle[-1]][cycle[0]]["weight"]
    return weights


def brute_force(g: nx.Graph) -> int:
    n = g.number_of_nodes()
    cycles = [cycle_length(g, p) for p in permutations(range(n))]
    return min(cycles)


def average(g: nx.Graph) -> float:
    n = g.number_of_nodes()

    sum_of_weights = sum(g[i][j]["weight"] for i in range(n) for j in range(i))
    return 2 * sum_of_weights / (n - 1)


def nearest_neighbors(g: nx.Graph) -> int:
    current_node = 0
    path = [current_node]
    n = g.number_of_nodes()

    for _ in range(n - 1):
        next_node = None
        min_edge = float("inf")

        for v in g.nodes():
            if g.has_edge(current_node, v) and v not in path:
                if g[current_node][v]["weight"] < min_edge:
                    min_edge = g[current_node][v]["weight"]
                    next_node = v

        assert next_node is not None
        path.append(next_node)
        current_node = next_node

    weight = sum(
        g[path[i]][path[i + 1]]["weight"] for i in range(g.number_of_nodes() - 1)
    )
    weight += g[path[-1]][path[0]]["weight"]
    return weight


def lower_bound(g: nx.Graph, sub_cycle: list) -> int:
    current_weight = sum(
        [g[sub_cycle[i]][sub_cycle[i + 1]]["weight"] for i in range(len(sub_cycle) - 1)]
    )

    unused = [v for v in g.nodes() if v not in sub_cycle]
    h = g.subgraph(unused)

    t = list(nx.minimum_spanning_edges(h))
    mst_weight = sum([h.get_edge_data(e[0], e[1])["weight"] for e in t])

    if len(sub_cycle) == 0 or len(sub_cycle) == g.number_of_nodes():
        return mst_weight + current_weight

    s = sub_cycle[0]
    t = sub_cycle[-1]
    min_to_s_weight = min([g[v][s]["weight"] for v in g.nodes() if v not in sub_cycle])
    min_from_t_weight = min(
        [g[t][v]["weight"] for v in g.nodes() if v not in sub_cycle]
    )

    return current_weight + min_from_t_weight + mst_weight + min_to_s_weight


def branch_and_bound(
    g: nx.Graph, sub_cycle: list = None, current_min: float = float("inf")
) -> int:
    if sub_cycle is None:
        sub_cycle = [0]

    if len(sub_cycle) == g.number_of_nodes():
        weight = sum(
            [
                g[sub_cycle[i]][sub_cycle[i + 1]]["weight"]
                for i in range(len(sub_cycle) - 1)
            ]
        )
        weight = weight + g[sub_cycle[-1]][sub_cycle[0]]["weight"]
        return weight

    unused_nodes = list()
    for v in g.nodes():
        if v not in sub_cycle:
            unused_nodes.append((g[sub_cycle[-1]][v]["weight"], v))

    unused_nodes = sorted(unused_nodes)

    for d, v in unused_nodes:
        assert v not in sub_cycle
        extended_subcycle = sub_cycle[:]
        extended_subcycle.append(v)
        if lower_bound(g, extended_subcycle) < current_min:
            new_sub_cycle = sub_cycle[:]
            new_sub_cycle.append(v)
            new_min = branch_and_bound(g, new_sub_cycle, current_min)
            if new_min < current_min:
                current_min = new_min
        return current_min


def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def dynamic_programming(g: nx.Graph) -> int:
    n = g.number_of_nodes()

    power = powerset(range(1, n))
    T = {}
    for i in range(1, n):
        T[(i,), i] = g[0][i]["weight"]

    for s in power:
        if len(s) > 1:
            for i in s:
                t = tuple([x for x in s if x != i])
                # TODO

    return min(T[tuple(range(1, n)), i] + g[i][0]["weight"] for i in range(1, n))


def approximation(g: nx.Graph) -> float:
    min_tree = nx.minimum_spanning_tree(g)
    depth_first_preorder = list(nx.dfs_preorder_nodes(min_tree, 0))
    result = 0
    for i in range(0, len(depth_first_preorder) - 1):
        result += g[depth_first_preorder[i]][depth_first_preorder[i + 1]]["weight"]
    result += g[depth_first_preorder[-1]][depth_first_preorder[0]]["weight"]

    return result


if __name__ == "__main__":
    g = nx.Graph()
    g.add_edge(0, 1, weight=2)
    g.add_edge(1, 2, weight=2)
    g.add_edge(2, 3, weight=2)
    g.add_edge(3, 0, weight=2)
    g.add_edge(0, 2, weight=1)
    g.add_edge(1, 3, weight=1)

    cycle1 = [0, 1, 2, 3]
    cycle2 = [0, 2, 1, 3]

    assert cycle_length(g, cycle1) == 8
    assert cycle_length(g, cycle2) == 6

    print(brute_force(g))
    print(average(g))
    print(nearest_neighbors(g))
    print(branch_and_bound(g))
    # print(dynamic_programming(g))

    coordinates = [
        (181, 243),
        (101, 143),
        (100, 216),
        (167, 15),
        (37, 201),
        (163, 226),
        (2, 42),
        (35, 73),
        (85, 116),
        (142, 235),
        (200, 18),
    ]
    optimal_cycle = [0, 5, 9, 2, 4, 1, 8, 7, 6, 3, 10]
    g = get_graph(coordinates)
    print(approximation(g))
