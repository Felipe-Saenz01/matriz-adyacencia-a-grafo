<h1 align="center" >Generar Grafo en Prolog a partir de Matriz de adyacencia</h1></br>
<p>Este Script de Python tiene como objetivo generar un grafo de prolog a partir de una matriz de adyacencia en un archivo .xlsx para no tener que hacerlo manual como en mi caso que queria hacer un grafo a partir de una amtriz hecha con la descendencia de Noé y es bastante grande.</p>

# Estructura Grafo de prolog
``` prolog
% estructura
% grafo([lista-elementos],[lista-relaciones/aristas]).

%ejemplo
grafo([noe, sem, cam, jafet],
[
  arista(noe, sem, padre),
  arista(noe, cam, padre),
  arista(noe, jafet, padre),
  arista(sem, cam, hermano),
  arista(sem, jafet, hermano),
  arista(cam, jafet, hermano),
]).
```

# Pasos para crear entorno virtual Python 
evidentemente es necesario tener Python instalado en el sistema

``` bash
git clone git@github.com:Felipe-Saenz01/matriz-adyacencia-a-grafo.git
cd matriz-adyacencia-a-grafo
python -m venv matriz
.\matriz\Scripts\activate
pip install pandas
pip install openpyxl
```

# Utilizar script y generar fichero .txt 
```
python matriz.py
```

