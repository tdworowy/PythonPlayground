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
