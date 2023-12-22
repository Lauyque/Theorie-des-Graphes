# Theorie-des-Graphes
#
#

# Question 7 de l'Exo 1

1.7
Voici les points :
- Placement automatique des sommets

- Complexité visuelle : Pour les grands graphes, le dessin peut devenir très encombré et difficile à lire.





# Exo 4 #



import matplotlib. pyplot as plt
import network x as nx
from numpy import array

# Définit ion du graphe
G = nx.Graph()

# Définition des noeuds
G.add_node(O,label='A' ,col='pink')
G.add_node(l,label='B' ,col='red')
G.add_node(2,label='C' ,col='white')
G.add_node(3,label='D' ,col='white')
G.add_node(4,label='E' ,col='white')
G.add_node(5,label='F' ,col='blue')

# Définition des aretes
G. add_edge (O, 1, weight =6)
G. add_edge (0, 2, weight = 5)
G.add_edge(0,4,weight=l)

G. add_edge (4, 1, weight = 5 )
G.add_edge(4,2,weight = 1)
G. add_edge (4, 3, weight = 3 )
G.add_edge(2,3,weight=8)
G. add_edge (4, 5, weight = 6)
G.add_edge(3,5,weight=9)

# Reprisentation du graphe basique
nx.draw(G)
p 1 t . show ()

# Traitement des noeuds:
# Colorer les noeuds
liste = list (G. nodes (data =' col'))
colorNodes = {}
for noeud in liste:
    colorNodes[noeud[O]]= noeud[l]
    print ( colorNodes )

# Pour colorer les noeuds, le format doit être une liste
colorList=[colorNodes [node] for node in colorNodes]
print ( colorList)

# Etiquetter les noeuds : le format doit être un dictionnaire
liste = list (G. nodes (data=' label'))
labels_nodes = {}
for noeud in liste:
labels_nodes [noeud [O]] = noeud [1]
print ( labels_nodes )
Traitement des sommets :

# Pour les it1quettes des arrêtes, le format doit être un dictionnaire
labels_edges = {}
labels_edges = { edge:G.edges[edge]['weight'] for edge in G.edges}
print(labels_edges)

# Une autre rédaction si celle ci-dessus pose problème
# Pour les itiquettes des arrêtes , le format doit être un dictionnaire
liste_edge = list(G.edges(data ='weight'))
labels_edges = {}
for edge in liste_edge
    labels_edges [edge [O] , edge [1]] = edge [1]
    print ( labels_edges)

# Représentation du graphe :
# Positions des sommets
pos = nx. spring_layout (G)

# Sommets :
nx.draw_networkx_nodes(G, pos, node_size=70 0,node_color=colorList ,alpha=0.9)

# Etiquettes des sommeto
nx.draw_networkx_labels(G, pos, labels= labels_nodes, \
with_labels=True,font_size=2 0, \
font_color ='black', \
font_family='sans-serif')

# Arrêtes :
nx.draw_networkx_edges(G, pos,width = l)
nx. draw_networkx_edge_labels (G, pos, width=l, edge_labels = labels_edges,
font_color ='red')
plt.axis('off')
plt. show()