import osmnx as ox
import networkx  as nx
from agent.grafo import nodos_mas_cercanos

def calcular_ruta_y_long(G, origen_lat, origen_lon, destino_lat, destino_lon):
    """Calcula la ruta más corta

    Args:
        G (_type_): grafo
        origen_lat (int,float): _description_
        origen_lon (int,float): _description_
        destino_lat (int,float): _description_
        destino_lon (int,float): _description_
    """
    # Convierte coordenadas a nodos más cercanos
    origen_node, destino_node = nodos_mas_cercanos\
        (G, origen_lat, origen_lon, destino_lat, destino_lon)
    
    # Error si el nodo de origen y destino son iguales
    if origen_node == destino_node:
        raise ValueError(f"Las coordenadas son muy cercanas la una a la otra")
    
    # Ruta nodo a nodo
    ruta_nodos = nx.shortest_path(G, origen_node, destino_node, weight='length')
    # Longitud de la ruta en metros
    ruta_longitud = nx.shortest_path_length(G, origen_node, destino_node, weight='length')
    
    return ruta_nodos, ruta_longitud