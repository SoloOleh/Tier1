import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("A")
G.add_nodes_from(["B", "C", "D"])

G.add_edge("A", "B")
G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D")])

num_nodes = G.number_of_nodes()  # 4
num_edges = G.number_of_edges()  # 4
is_connected = nx.is_connected(G)  # True

degree_centrality = nx.degree_centrality(G)  # {'A': 0.6666666666666666, 'B': 1.0, 'C': 0.6666666666666666, 'D': 0.3333333333333333}
closeness_centrality = nx.closeness_centrality(G)  # {'A': 0.75, 'B': 1.0, 'C': 0.75, 'D': 0.6}
betweenness_centrality = nx.betweenness_centrality(G)  # {'A': 0.0, 'B': 0.6666666666666666, 'C': 0.0, 'D': 0.0}

path = nx.shortest_path(G, source="A", target="D")  # ['A', 'B', 'D']
avg_path_length = nx.average_shortest_path_length(G)  # 1.3333333333333333

import matplotlib.pyplot as plt
G = nx.complete_graph(8)
nx.draw(G, with_labels=True)
plt.show()

networkx.draw(G, pos=None, ax=None, **kwds)

import matplotlib.pyplot as plt
G = nx.complete_graph(4)
options = {
    "node_color": "yellow",
    "edge_color": "lightblue",
    "node_size": 500,
    "width": 3,
    "with_labels": True
}
nx.draw(G, **options)
plt.show()

