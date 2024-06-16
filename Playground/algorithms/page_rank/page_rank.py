import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def create_page_rank(graph: nx.DiGraph) -> tuple:
    nodes_set = len(graph)
    m = nx.to_numpy_matrix(graph)
    outwards = np.squeeze(np.asarray(np.sum(m, axis=1)))
    prob_outwards = np.array([1.0 / count if count > 0 else 0.0 for count in outwards])
    transition_matrix = np.asarray(np.multiply(m.T, prob_outwards))
    p = np.ones(nodes_set) / float(nodes_set)

    if np.min(np.sum(transition_matrix, axis=0)) < 1.0:
        print("WARN: transition_matrix is substochastic")

    return transition_matrix, p


if __name__ == "__main__":
    my_web = nx.DiGraph()
    my_pages = range(1, 5)

    connections = [
        (1, 3),
        (2, 1),
        (2, 3),
        (3, 1),
        (3, 2),
        (3, 4),
        (4, 5),
        (5, 1),
        (5, 4),
    ]

    my_web.add_nodes_from(my_pages)
    my_web.add_edges_from(connections)

    pos = nx.shell_layout(my_web)
    nx.draw(my_web, pos, arrows=True, with_labels=True)
    plt.show()

    transition_matrix, p = create_page_rank(my_web)
    print(transition_matrix)
    print(p)
