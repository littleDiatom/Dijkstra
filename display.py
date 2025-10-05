import matplotlib.pyplot as plt
import networkx as nx

class Display:
    def __init__(self, graph, minimal_distance, previous_nodes, start=None, end=None):
        """
        graph : dict -> graphe d’adjacence avec les poids
        minimal_distance : dict -> distances minimales calculées par Dijkstra
        previous_nodes : dict -> noeuds précédents pour reconstruire le chemin
        start, end : str -> noms des noeuds de départ et d’arrivée
        """
        self.graph = graph
        self.minimal_distance = minimal_distance
        self.previous_nodes = previous_nodes
        self.start = start
        self.end = end

    def minimal_path(self):
        """Reconstruit le chemin minimal à partir des précédents noeuds"""
        if self.end is None:
            return []
        path = []
        current = self.end
        while current is not None:
            path.append(current)
            current = self.previous_nodes.get(current)
        path.reverse()
        return path

    def draw_graph(self):
        """Affiche le graphe initial avec le chemin minimal en rouge"""
        G = nx.DiGraph()

        # Construire le graphe à partir du dictionnaire d’adjacence
        for node, neighbors in self.graph.items():
            for neighbor, weight in neighbors.items():
                G.add_edge(node, neighbor, weight=weight)

        # === Layout hiérarchique (Graphviz 'dot') ===
        # → Chaque couche correspond à un "niveau" dans le graphe
        pos = nx.nx_agraph.graphviz_layout(G, prog='dot')

        plt.figure(figsize=(14, 8))

        # --- Arêtes de base (grises) ---
        nx.draw_networkx_edges(G, pos, edge_color='gray', width=1.5, arrows=True, alpha=0.6)

        # --- Nœuds normaux ---
        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=1800, edgecolors='black')

        # --- Labels des nœuds ---
        nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

        # --- Labels des poids sur les arêtes ---
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black', label_pos=0.5)

        # --- Chemin minimal en rouge ---
        if self.start and self.end:
            path = self.minimal_path()
            if len(path) > 1:
                path_edges = list(zip(path[:-1], path[1:]))
                nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3, arrows=True)

        plt.title(f"Chemin minimal de {self.start} à {self.end}", fontsize=14)
        plt.axis('off')
        plt.tight_layout()
        plt.savefig("graph.png", dpi=300)
