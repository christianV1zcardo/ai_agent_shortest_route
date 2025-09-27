import osmnx as ox


# Ciudad del Grafo
place = "San Isidro, Lima, Peru"

def crear_grafo(place):
    G = ox.graph.graph_from_place(place, network_type='drive')
    return G