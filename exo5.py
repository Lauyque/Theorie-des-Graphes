import networkx as nx
import matplotlib.pyplot as plt

# Définition des positions des nœuds
node_positions = {
    9: (5, 0),5: (3, 1),3: (2, 2),6: (4, 2),8: (5, 2),1: (1, 3),4: (3, 3),2: (2, 4),7: (5, 4)
}

# Initialisation du graphe
G = nx.Graph()

# Ajout des arêtes avec les poids
edges_with_labels = [
    (1, 2, '2'),(2, 7, '3'),(1, 3, '1'),(2, 4, '1'),(7, 8, '5'),(4, 6, '3'),(6, 7, '4'),(2, 3, '2'),(3, 5, '5'),(4, 5, '3'),(5, 6, '1'),(6, 9, '3'),(8, 9, '2'),(8, 6, '1')
]

# Ajout des arêtes au graphe
G.add_weighted_edges_from([(u, v, float(w)) for u, v, w in edges_with_labels])

# Fonction pour tester si le graphe a des sommets isolés
def testnonisole(G):
    return all(degree > 0 for node, degree in G.degree())

# Fonction pour trouver l'arbre couvrant de poids minimal
def AlgoACM(G):
    if nx.is_connected(G):
        T = nx.minimum_spanning_tree(G)
        poids = sum(weight for (u, v, weight) in T.edges.data('weight'))
        return T, poids
    else:
        return None, None

# Affichage du graphe initial
plt.figure(figsize=(15, 8))  # Augmenter la hauteur de la figure
nx.draw(G, pos=node_positions, with_labels=True, node_size=1000, node_color='white', 
        font_size=12, font_color='black', font_weight='bold', edge_color="gray", linewidths=1, 
        edgecolors='black')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos=node_positions, edge_labels=edge_labels, label_pos=0.3)
plt.title("Graphe original avec étiquettes des sommets et poids des arêtes", pad=20)  # Ajouter un espace ('pad') sous le titre
plt.axis('off')
plt.show()

# Vérification des sommets isolés
print("Le graphe G a des sommets isolés:", not testnonisole(G))

# Application de l'algorithme ACM et affichage de l'arbre couvrant minimal
T, poids = AlgoACM(G)
if T:
    plt.figure(figsize=(15, 8))  # Augmenter la hauteur de la figure
    nx.draw(T, pos=node_positions, with_labels=True, node_size=1000, node_color='white', 
            font_size=12, font_color='black', font_weight='bold', edge_color="red", linewidths=1, 
            edgecolors='black')
    edge_labels = nx.get_edge_attributes(T, 'weight')
    nx.draw_networkx_edge_labels(T, pos=node_positions, edge_labels=edge_labels, label_pos=0.3)
    plt.title(f"Arbre couvrant minimal de poids {poids}", pad=20)  # Ajouter un espace ('pad') sous le titre
    plt.axis('off')
    plt.show()
else:
    print("Le graphe n'est pas connexe, donc il n'existe pas d'arbre couvrant minimal.")
