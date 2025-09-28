from agent.ruta import calcular_ruta_y_long
from flask import Flask, request, jsonify
from flask_cors import CORS
import osmnx as ox

filepath = 'data/san_isidro.graphml'

app = Flask(__name__)
CORS(app)

G = ox.load_graphml(filepath)

@app.route("/route", methods=['POST'])
def calcular_ruta():
    # Obtener JSON del click enviado por el cliente
    data = request.get_json()
    
    # Extraer coordenadas
    origen_lat = data['origen']['lat']
    origen_lon = data['origen']['lon']
    destino_lat = data['destino']['lat']
    destino_lon = data['destino']['lon']
    
    # Convertir coordenadas a nodos del grafo y obtener ruta y distancia
    ruta_nodos, ruta_longitud = calcular_ruta_y_long\
        (G, origen_lat, origen_lon, destino_lat, destino_lon)
    
    # DUDAS
    # Transformar ruta de nodos a coordenadas
    ruta_coords = [{'lat': G.nodes[n]['y'], 'lon': G.nodes[n]['x']} for n in ruta_nodos]
    
    # Devolver resultado en JSON
    return jsonify({'distancia': ruta_longitud, 'ruta': ruta_coords})



if __name__ == "__main__":
    app.run(debug=True)