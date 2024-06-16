import networkx as nx
import matplotlib.pyplot as plt


def breadth_first_search(graph: dict, start: str) -> list:
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited


if __name__ == "__main__":
    graph = {
        "Amin": {"Wasim", "Nick", "Mike"},
        "Wasim": {"Imran", "Amin"},
        "Imran": {"Wasim", "Faras"},
        "Faras": {"Imran"},
        "Mike": {"Amin"},
        "Nick": {"Amin"},
    }

    res1 = breadth_first_search(graph, "Amin")
    res2 = breadth_first_search(graph, "Mike")

    graph1 = nx.DiGraph(graph)

    print(res1)
    print(res2)

    nx.draw(graph1, with_labels=True, node_color="y", node_size=800)
    plt.show()
