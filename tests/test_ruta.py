import pytest
from src.ruta import calcular_ruta_y_long

def test_tipos_calcular_ruta_y_long():
    with pytest.raises(TypeError): 
        calcular_ruta_y_long("grafo", "coordenada", "coordenada",
                             "coordenada","coordenada")