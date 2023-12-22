import matplotlib. pyplot as plt # Pour les graphiques
import networkx as nx # Pour les graphes
from numpy import array # Pour les matrices

# Définit ion du graphe
G = nx.Graph() # Graphe non orienté 

# Définition des noeuds
G.add_node(O,label='A' ,col='pink') # Ajout du noeud 0
G.add_node(l,label='B' ,col='red') # Ajout du noeud 1
G.add_node(2,label='C' ,col='white') # Ajout du noeud 2
G.add_node(3,label='D' ,col='white') # Ajout du noeud 3
G.add_node(4,label='E' ,col='white') # Ajout du noeud 4
G.add_node(5,label='F' ,col='blue') # Ajout du noeud 5

# Définition des aretes
G. add_edge (O, 1, weight =6) # Ajout de l'arête (0, 1)
G. add_edge (0, 2, weight = 5) # Ajout de l'arête (0, 2)
G.add_edge(0,4,weight=l) # Ajout de l'arête (0, 4)

G. add_edge (4, 1, weight = 5 ) # Ajout de l'arête (4, 1)
G.add_edge(4,2,weight = 1)  # Ajout de l'arête (4, 2)
G. add_edge (4, 3, weight = 3 ) # Ajout de l'arête (4, 3)
G.add_edge(2,3,weight=8)    # Ajout de l'arête (2, 3)
G. add_edge (4, 5, weight = 6)  # Ajout de l'arête (4, 5)
G.add_edge(3,5,weight=9)    # Ajout de l'arête (3, 5)

# Reprisentation du graphe basique
nx.draw(G)  # Dessin du graphe
plt.show() # Affichage du graphe

# Traitement des noeuds:
# Colorer les noeuds
liste = list (G. nodes (data =' col')) # Liste des noeuds avec leurs couleurs
colorNodes = {} # Dictionnaire des couleurs des noeuds
for noeud in liste: # Parcours de la liste des noeuds
    colorNodes[noeud[O]]= noeud[l] # Ajout de la couleur du noeud
    print ( colorNodes ) # Affichage du dictionnaire des couleurs des noeuds

# Pour colorer les noeuds, le format doit être une liste
colorList=[colorNodes [node] for node in colorNodes] # Liste des couleurs des noeuds
print ( colorList) # Affichage de la liste des couleurs des noeuds

# Etiquetter les noeuds : le format doit être un dictionnaire
liste = list (G. nodes (data=' label')) # Liste des noeuds avec leurs étiquettes
labels_nodes = {} # Dictionnaire des étiquettes des noeuds
for noeud in liste:     # Parcours de la liste des noeuds
    labels_nodes[noeud [O]] = noeud [1] # Ajout de l'étiquette du noeud
print ( labels_nodes ) # Affichage du dictionnaire des étiquettes des noeuds

#Traitement des sommets :

# Pour les it1quettes des arrêtes, le format doit être un dictionnaire
labels_edges = {} # Dictionnaire des étiquettes des arrêtes
labels_edges = { edge:G.edges[edge]['weight'] for edge in G.edges}  # Ajout des étiquettes des arrêtes
print(labels_edges) # Affichage du dictionnaire des étiquettes des arrêtes

# Une autre rédaction si celle ci-dessus pose problème
# Pour les itiquettes des arrêtes , le format doit être un dictionnaire
liste_edge = list(G.edges(data ='weight')) # Liste des arrêtes avec leurs étiquettes
labels_edges = {} # Dictionnaire des étiquettes des arrêtes
for edge in liste_edge : # Parcours de la liste des arrêtes
    labels_edges [edge [O] , edge [1]] = edge [1]   # Ajout de l'étiquette de l'arrête
    print ( labels_edges)   # Affichage du dictionnaire des étiquettes des arrêtes

# Représentation du graphe :
# Positions des sommets
pos = nx.spring_layout (G) # Positions des sommets

# Sommets :
nx.draw_networkx_nodes(G, pos, node_size=700,node_color=colorList ,alpha=0.9) # Dessin des sommets

# Etiquettes des sommets , avec_labels=True pour afficher les étiquettes des sommets
nx.draw_networkx_labels(G, pos, labels= labels_nodes, \
    with_labels=True,font_size=20, \
    font_color ='black', \
    font_family='sans-serif')

# Arêtes , width=l pour afficher les poids des arrêtes 
nx.draw_networkx_edges(G, pos,width = l) # Dessin des arrêtes
nx.draw_networkx_edge_labels(G, pos, width=l, edge_labels=labels_edges, # Dessin des étiquettes des arrêtes
font_color ='red') # Couleur des étiquettes des arrêtes 
plt.axis('off') # Suppression des axes 
plt. show() # Affichage du graphe