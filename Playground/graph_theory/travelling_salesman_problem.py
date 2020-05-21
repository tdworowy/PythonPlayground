import networkx as nx
from itertools import permutations


def cycle_length(g: nx.Graph, cycle: list) -> int:
    assert len(cycle) == g.number_of_nodes()
    weights = 0
    for i in range(len(cycle) - 1):
        weights += g[cycle[i]][cycle[i + 1]]['weight']
    weights += g[cycle[-1]][cycle[0]]['weight']
    return weights


def brute_force(g: nx.Graph) -> int:
    n = g.number_of_nodes()
    cycles = [cycle_length(g, p) for p in permutations(range(n))]
    return min(cycles)


def average(g: nx.Graph) -> float:
    n = g.number_of_nodes()

    sum_of_weights = sum(g[i][j]['weight'] for i in range(n) for j in range(i))
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
                if g[current_node][v]['weight'] < min_edge:
                    min_edge = g[current_node][v]['weight']
                    next_node = v

        assert next_node is not None
        path.append(next_node)
        current_node = next_node

    weight = sum(g[path[i]][path[i + 1]]['weight'] for i in range(g.number_of_nodes() - 1))
    weight += g[path[-1]][path[0]]['weight']
    return weight


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

    assert (cycle_length(g, cycle1) == 8)
    assert (cycle_length(g, cycle2) == 6)

    print(brute_force(g))
    print(average(g))
    print(nearest_neighbors(g))
