from graph import Graph
from display import Display

def main_non_oriented():
    graph = Graph({
            'A': {'B': 10, 'F': 9},
            'B': {'E': 13, 'D': 8, 'C': 5},
            'F': {'E': 15, 'D':5, 'C': 3},
            'E': {'F':15, 'D': 2, 'B': 13},
            'C': {'B': 5, 'D': 4, 'F': 3},
            'D': {'B': 8, 'C': 4, 'E':1, 'F':5}
        }, 'A')
    distances = graph.dijkstra()
    print("Result:", distances)


def main_oriented():
    graph= Graph({
            'S': {'A':5, 'B':3, 'C':2},
            'A': {'D':2, 'E':2},
            'B': {'A':1},
            'C': {'B':1, 'E':3, 'F':2},
            'E': {'F':4},
            'D': {'E':4,'T':7},
            'F': {'T':6, 'D':10},
            'T': {}
    }, 'S')
    distances = graph.dijkstra()
    print("Result:", distances)


def tresor():
    graph_data={
        'depart': {'ville': 4, 'foret': 1},
        'ville': {'capitale': 3, 'col du nord':5},
        'foret': {'ville': 2, 'capitale': 7},
        'capitale': {'palais': 10, 'refuge': 4},
        'col du nord': {'refuge': 3},
        'refuge': {'palais': 5, "épée": 10, "dragon": 32},
        'palais': {'bibliothèque': 6},
        'bibliothèque': {'tresor': 30, 'épée': 7},
        'épée': {'dragon': 8, 'tresor': 18},
        'dragon': {'tresor': 9},
        'tresor': {}
    }
    graph = Graph(graph_data, 'depart')
    distances, previous_nodes = graph.dijkstra()
    Display(graph_data,distances, previous_nodes, 'depart', 'tresor').draw_graph()

if __name__ == "__main__":
    tresor()