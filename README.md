# Algorithme de Dijkstra

L’algorithme de Dijkstra sert à trouver le chemin le plus court entre un point de départ et tous les autres points d’un graphe (par exemple : des villes reliées par des routes avec des distances).

## Description

Ce petit projet contient une implémentation pédagogique de l'algorithme de Dijkstra en Python, ainsi que des outils simples pour visualiser un graphe et sauvegarder son rendu.

Fichiers principaux :
- `graph.py` : implémentation de la structure de graphe et de l'algorithme de Dijkstra.
- `display.py` : fonctions de visualisation (utilise `networkx` et `matplotlib`).
- `main.py` : exemples d'utilisation et scénario "tresor".

## Prérequis

- Python 3.10+
- pip
- Les paquets Python : `networkx`, `matplotlib` et `pygraphviz` 

Pour installer rapidement les dépendances Python :

```bash
pip install networkx matplotlib pygraphviz
```

## Exécution

Depuis la racine du projet (où se trouve `main.py`) :

```bash
python3 main.py
```

Cela exécutera le scénario `tresor` défini dans `main.py`. Le script affiche les distances calculées par Dijkstra et génère un fichier `graph.png` contenant la visualisation du graphe.

## Exemple de sortie

```
Result: {'depart': 0, 'foret': 1, 'ville': 4, ... 'tresor': 20}
```

Et le fichier `graph.png` sera créé dans le dossier du projet.

## Extensions possibles

- Exporter les chemins les plus courts trouvés dans un fichier JSON/CSV.
- Améliorer la mise en page du graphe en utilisant les layouts fournis par Graphviz (via `pygraphviz`) pour des graphes plus grands.


## Scénario Tresor
On considère le problème suivant :

Le prince est parti à la recherche du trésor. Il peut accomplir les actions suivantes :

- Aller à la ville du marché, en contournant la rivière par un gué : **4 jours**
- Traverser la forêt : **1 jour**
- Depuis la forêt, abattre des arbres pour traverser la rivière, et se rendre à la ville du marché : **2 jours**
- Depuis la forêt, se rendre à la capitale provinciale en traversant les marais : **7 jours**
- S’équiper chaudement au marché, et partir pour le col du nord : **5 jours**
- Trouver un bon cheval au marché, et se rendre à la capitale provinciale par la grand-route : **3 jours**
- Depuis le col du nord, se rendre au refuge du devin : **3 jours**
- Depuis la capitale provinciale, se rendre au refuge du devin : **4 jours**
- Se rendre de la capitale provinciale au palais du roi, en étant retardé par des contrôles : **10 jours**
- Au sortir du devin, partir directement chercher l’épée, et la trouver après s’être perdu par manque de carte : **20 jours**
- Au sortir de chez le devin, au mépris de ses avis, se rendre directement à la grotte et tuer le dragon avec un canif : **32 jours** (il faut du temps pour le tuer avec un canif)
- Bien conseillé par le devin, prendre un raccourci pour le palais du roi : **5 jours**
- Une fois arrivé au palais du roi, séduire la bibliothécaire, puis trouver les cartes qui expliquent l’emplacement de l’épée et du trésor : **6 jours**
- En utilisant les cartes trouvées dans la bibliothèque, faire tout le tour de la montagne, et traverser un labyrinthe qui mène directement au trésor : **30 jours**
- En utilisant les cartes, aller chercher l’épée pour combattre le dragon : **7 jours**
- S’entraîner à l’épée, puis tuer le dragon : **8 jours**
- Une fois l’épée trouvée, au lieu d’affronter le dragon, utiliser l’épée pour creuser un tunnel par dessous, et déboucher directement dans la cachette du trésor : **18 jours**
- Une fois le dragon tué, résoudre l’énigme qui ouvre la cachette du trésor : **9 jours**

**Question :**  
Comment doit-il faire pour récupérer le trésor le plus vite possible ? Quel temps lui faudra-t-il ?


