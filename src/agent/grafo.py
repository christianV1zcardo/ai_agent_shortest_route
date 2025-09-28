import osmnx as ox


# Ciudad del Grafo
place = "San Isidro, Lima, Peru"

def crear_grafo(place):
    G = ox.graph.graph_from_place(place, network_type='drive')
    return G

def nodos_mas_cercanos(G, origen_lat, origen_lon, destino_lat, destino_lon):
    """Recibe el grafo y las coordenadas para retornar los nodos más cercanos

    Args:
        G (_type_): _description_
        origen_lat (_type_): _description_
        origen_lon (_type_): _description_
        destino_lat (_type_): _description_
        destino_lon (_type_): _description_

    Raises:
        TypeError: _description_

    Returns:
        _type_: _description_
    """
    args = [origen_lat, origen_lon, destino_lat, destino_lon]

    if not all(isinstance(arg, (float, int)) for arg in args):
        raise TypeError(f"Las coordenadas deben ser numéricas (float o int)")
    
    origen_node = ox.distance.nearest_nodes(G, origen_lon, origen_lat)
    destino_node = ox.distance.nearest_nodes(G, destino_lon, destino_lat)
    
    return origen_node, destino_node