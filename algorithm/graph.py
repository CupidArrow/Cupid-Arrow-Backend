import json
import networkx as nx
import matplotlib.pyplot as plt
from ufds import UFDS

def plot_person_graph(G, labels):
    plt.figure(figsize=(16, 9))
    pos = nx.spring_layout(G, k=0.35, iterations=50)  # Ajusta los parámetros para minimizar la superposición
    node_colors = [node[1].get('color', 'gray') for node in G.nodes(data=True)]

    nx.draw_networkx_nodes(G, pos, node_color=node_colors)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, labels, font_size=12)

    plt.axis('off')
    manager = plt.get_current_fig_manager()
    manager.window.state('zoomed')
    plt.show()

def create_person_graph(city, gender, interest, data):
    G = nx.Graph()
    ufds = UFDS(len(data) + 1)  # +1 para incluir el nodo 'You'
    labels = {}

    # Agregar nodos para personas que cumplen con los criterios
    for i, person in enumerate(data):
        if person['city'] == city and person['sex'] == gender and interest in person.get('interests', []):
            G.add_node(person['id'], color='green')
            G.add_edge('You', person['id'], color='green')
            ufds.union(0, i+1)  # asumimos que 'You' es el nodo 0
            labels[person['id']] = person['name']

    # Imprimir solo el conjunto que contiene a 'You'
    print("Estás conectado/a con:")
    for i in range(1, len(data) + 1):
        if ufds.connected(0, i):
            print(data[i-1]['name'])

    return G, labels

# Crear y mostrar el grafo


# Cargar los datos del archivo JSON
with open('../data/data.json') as f:
    data = json.load(f)

# Obtener la entrada del usuario para el género, interés y ciudad
gender = input('Ingresa su género (mujer/varon): ')
interest = input('Ingresa un interés: ')
city = input('Ingresa una ciudad: ')

# Crear y mostrar el grafo
G, labels = create_person_graph(city, gender, interest, data)
plot_person_graph(G, labels)