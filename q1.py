import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# Estados
G.add_node("q0")
G.add_node("q1")
G.add_node("qf")

# Transições
G.add_edge("q0", "q0", label="⟨/⟨,D")
G.add_edge("q0", "q1", label="a/⊔,D")
G.add_edge("q1", "q0", label="a/⊔,D")
G.add_edge("q0", "qf", label="⊔/⊔,D")

pos = {
    "q0": (0, 0),
    "q1": (2, 0),
    "qf": (1, -2)
}

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=3000,
    font_size=12
)

labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.axis('off')
plt.show()