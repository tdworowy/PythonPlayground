import networkx as nx
import matplotlib.pyplot as plt


def depth_first_search(graph: dict, start: str, visited: set = None) -> set:
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next_ in graph[start] - visited:
        depth_first_search(graph, next_, visited)
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

    res1 = depth_first_search(graph, "Amin")
    print("_" * 10)
    res2 = depth_first_search(graph, "Mike")

    graph1 = nx.DiGraph(graph)

    print(res1)
    print(res2)

    nx.draw(graph1, with_labels=True, node_color="y", node_size=800)
    plt.show()
