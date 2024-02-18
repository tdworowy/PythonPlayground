from typing import Iterable

import networkx as nx
import matplotlib.pyplot as plt
from random import choice


def generate_edges(vertices: Iterable, edges_count: int) -> list:
    result = []
    for _ in range(edges_count):
        x = choice(vertices)
        y = choice(vertices)
        while x == y:
            y = choice(vertices)

        result.append((x, y))
    return result


if __name__ == "__main__":
    vertices = range(1, 10)
    edges = generate_edges(vertices, 30)

    graph = nx.Graph()
    graph.add_nodes_from(vertices)
    graph.add_edges_from(edges)

    nx.draw(graph, with_labels=True, node_color='y', node_size=800)
    plt.show()

    print(f"Degree centrality: {nx.degree_centrality(graph)}")
    print(f"Betweenness: {nx.betweenness_centrality(graph)}")
    print(f"Closeness: {nx.closeness_centrality(graph)}")
    print(f"Eigenvector: {nx.eigenvector_centrality(graph)}")
