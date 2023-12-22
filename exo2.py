import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Création des graphes
G = nx.Graph()  # Graphe non orienté
DG = nx.Graph()  # Graphe orienté

# Ajout de sommets aux graphes
for i in range(1, 6):
    G.add_node(i)
    DG.add_node(i)

# Affichage des sommets des graphes
print("Sommet de G :", G.nodes())
print("Sommet de DG:", DG.nodes())

# Ajout d'arêtes au graphe G
G.add_edges_from([(1,2),(2, 3), (2, 5), (3, 4), (4, 5),(4,6),(6,7),(7,5),(7,8),(8,9),(9,5),(9,1)])

# Ajout d'arêtes au graphe DG
DG.add_edges_from([(1, 3), (1, 2), (2, 3), (4, 5), (4, 6), (5, 6)])


# Position manuelle des positions des nœuds
node_positions_G = {1: (0, 0),2: (1, 0),3: (2, 0),  4: (2, 1),5: (1, 1),6: (2, 2),  7: (1, 2),8: (0, 2),9: (0, 1)   }
node_positions_GD = {1: (0, 1), 2: (-0.87, -0.5), 3: (0.87, -0.5), 4: (0, -1), 5: (0.87, 0.5), 6: (-0.87, 0.5)}

# Tracé des graphes
plt.figure()

nx.draw(G,pos=node_positions_G, with_labels=True)
plt.show()

plt.figure()
nx.draw(DG,pos=node_positions_GD, with_labels=True)
plt.show()