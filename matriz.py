import pandas as pd

def read_adjacency_matrix(file_path):
    # Lee la matriz de adyacencia desde el archivo .xlsx
    df = pd.read_excel(file_path, index_col=0)

    return df

def generate_prolog_graph(matrix):
    # Obtiene los nombres de las personas (nodos)
    nodes = list(matrix.index)
    nodes_str = ", ".join(nodes)  # Une los nombres sin comillas

    # Genera la lista de aristas
    edges = []
    for i, row in matrix.iterrows():
        for j, value in row.items():
            if value != 0:  # Si hay una arista
                edges.append(f"    arista({i}, {j}, {value}),")

    # Crea el objeto de Prolog
    graph_str = f"grafo([{nodes_str}],\n[ \n"
    for edge in edges:
        # Elimina las comillas alrededor de 'i' y 'j'
        edge = edge.replace("'", "")
        graph_str += f"  {edge}\n"
    graph_str = graph_str[:-3] + "\n])\n"  # Eliminar la última coma y agregar salto de línea

    return graph_str

def save_prolog_graph_to_txt(graph_str, filename):
    """
    Guarda el string del grafo Prolog en un archivo .txt con saltos de línea.

    Args:
        graph_str (str): El string que representa el grafo Prolog.
        filename (str): El nombre del archivo .txt donde se guardará el grafo.
    """
    with open(filename, 'w') as f:
        f.write(graph_str)

if __name__ == "__main__":
    file_path = "Matriz-de-adyacencia-Descendencia-de-Noe.xlsx"
    adjacency_matrix = read_adjacency_matrix(file_path)
    prolog_graph_str = generate_prolog_graph(adjacency_matrix)
    save_prolog_graph_to_txt(prolog_graph_str, "grafo_descendencia_noe.txt")
    print("Grafo guardado en 'grafo_descendencia_noe.txt'.")
