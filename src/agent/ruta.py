import osmnx as ox
import networkx  as nx

def calcular_ruta_y_long(G, origen_lat, origen_lon, destino_lat, destino_lon):
    """Calcula la ruta más corta

    Args:
        G (_type_): grafo
        origen_lat (int,float): _description_
        origen_lon (int,float): _description_
        destino_lat (int,float): _description_
        destino_lon (int,float): _description_
    """

    # Se verifica que las coordenadas tengan el tipo correcto
    args = [origen_lat, origen_lon, destino_lat, destino_lon]

    if not all(isinstance(arg, float, int) for arg in args):
        raise TypeError(f"Las coordenadas deben ser numéricas (float o int)")
    
    
    # Obtiene los nodos más cercanos de las latitudes
    origen_node = ox.distance.nearest_nodes(G, origen_lon, origen_lat)
    destino_node = ox.distance.nearest_nodes(G, destino_lon, destino_lat)
    
    # Ruta nodo a nodo
    ruta = nx.shortest_path(G, origen_node, destino_node, weight='length')
    # Longitud de la ruta en metros
    ruta_longitud = nx.shortest_path_length(G, origen_node, destino_node, weight='length')
    
    return ruta, ruta_longitud