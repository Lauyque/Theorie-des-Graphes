import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Création des graphes
G = nx.Graph()  # Graphe non orienté
DG = nx.DiGraph()  # Graphe orienté

# Ajout de sommets aux graphes
for i in range(1, 6):
    G.add_node(i)
    DG.add_node(i)

# Affichage des sommets des graphes
print("Sommet de G:", G.nodes())
print("Sommet de DG:", DG.nodes())

# Suppression du sommet 1 du graphe G
G.remove_node(1)

# Ajout d'arêtes au graphe G
G.add_edges_from([(2, 3), (2, 5), (3, 4), (4, 5)])

# Ajout d'arêtes au graphe DG
DG.add_edges_from([(1, 3), (2, 3), (2, 4), (2, 5), (4, 5), (5, 1)])

# Tracé des graphes
plt.figure()
nx.draw(G, with_labels=True)
plt.show()

plt.figure()
nx.draw(DG, with_labels=True)
plt.show()