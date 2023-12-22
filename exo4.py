import networkx as nx
import matplotlib.pyplot as plt
from numpy import random

def creer_graphe_aleatoire():
    nb_sommets = random.randint(2, 17)
    G = nx.Graph()
    
    for i in range(nb_sommets):
        G.add_node(i)
    
    for i in range(nb_sommets):
        for j in range(i+1, nb_sommets):
            if random.rand() > 0.5:
                G.add_edge(i, j)
    
    return G

G_aleatoire = creer_graphe_aleatoire()
pos = nx.spring_layout(G_aleatoire)
nx.draw_networkx_nodes(G_aleatoire, pos, node_color='blue', node_size=500)
nx.draw_networkx_edges(G_aleatoire, pos)
nx.draw_networkx_labels(G_aleatoire, pos, font_color='white')
plt.axis('off')
plt.show()