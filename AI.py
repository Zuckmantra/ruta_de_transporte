from pyDatalog import pyDatalog
import networkx as nx


G = nx.DiGraph()
G.add_weighted_edges_from([
    ("A", "B", 5),
    ("B", "C", 10),
    ("A", "D", 15),
    ("D", "C", 5),
    ("B", "D", 2),
    ("C", "E", 8),
    ("D", "E", 6)   
])


def encontrar_mejor_ruta(origen, destino):
    try:
        mejor_camino = nx.shortest_path(G, source=origen, target=destino, weight="weight")
        costo_total = nx.shortest_path_length(G, source=origen, target=destino, weight="weight")
        return mejor_camino, costo_total
    except nx.NetworkXNoPath:
        return None, None


origen = "A"
destino = "C"
ruta_optima, costo_total = encontrar_mejor_ruta(origen, destino)

if ruta_optima:
    print(f"Mejor ruta de {origen} a {destino}: {ruta_optima} con costo total de {costo_total}")
else:
    print(f"No hay ruta disponible de {origen} a {destino}")
