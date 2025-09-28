import osmnx as ox
import networkx as nx
import sklearn

from agent.grafo import crear_grafo
from agent.ruta import calcular_ruta_y_long

place = "San Isidro, Lima, Peru"
origen_lat, origen_lon = -12.10015, -77.05240
destino_lat, destino_lon = -12.10277, -77.03774


# Grafo
G = crear_grafo(place)

ruta, ruta_long = calcular_ruta_y_long(G, origen_lat, origen_lon, destino_lat, destino_lon)

print(f"La longitud de la ruta más corta es: {ruta_long} y la ruta es: {ruta}")