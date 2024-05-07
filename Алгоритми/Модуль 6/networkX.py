import networkx as nx

G = nx.Graph()

G.add_node("A")

G.add_nodes_from(["B", "C", "D"])

G.add_edge("A", "B")

G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D")])

print(G.nodes())  # ['A', 'B', 'C', 'D']

print(G.edges())  # [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D')]

print(list(G.neighbors("A")))  # ['B', 'C']

G.remove_node("A")

G.remove_nodes_from(["B", "C"])

# G.remove_edge("A", "B")

G.remove_edges_from([("A", "C"), ("B", "D")])

DG = nx.DiGraph()

DG.add_edge("A", "B")

DG.add_edge("B", "A")

G = nx.Graph()
G.add_edges_from([("A", "B"), ("B", "C")])
DG = nx.DiGraph(G)

G.add_node(1)
G.add_node("A")
G.add_node((2, 3))

G.add_edge(1, "A", weight=2.5, label="connection")

G.nodes[1]["color"] = "red"
G.edges[1, "A"]["label"] = "bridge"

neighbors_of_A = G["A"] # {'B': {}, 'C': {}}

edge_info = G["A"]["B"]  # {}

edge_weight = G["A"]["B"]["weight"]

G.graph["name"] = "My Graph"

G.nodes["A"]["color"] = "blue"

G["A"]["B"]["weight"] = 5

G.add_node("A", color="red")
G.add_edge("A", "B", weight=4)
