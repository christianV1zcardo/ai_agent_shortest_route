import pytest
from agent.ruta import calcular_ruta_y_long
from agent.grafo import crear_grafo

# Creo el grafo con latitudes para los tests
place = "San Isidro, Lima, Peru"
origen_lat, origen_lon = -12.10015, -77.05240
destino_lat, destino_lon = -12.10277, -77.03774

# Grafo
G = crear_grafo(place)

# Test de entradas
def test_tipos_calcular_ruta_y_long():
    with pytest.raises(TypeError): 
        calcular_ruta_y_long("grafo", "coordenada", "coordenada",
                             "coordenada","coordenada")
        
# Test de 
def test_origen_destino_igual():
    with pytest.raises(ValueError):
        calcular_ruta_y_long(G, origen_lat=origen_lat, 
                             origen_lon=origen_lon,
                             destino_lat=origen_lat, 
                             destino_lon=origen_lon)