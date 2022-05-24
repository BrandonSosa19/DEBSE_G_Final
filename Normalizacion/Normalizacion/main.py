
import archivo as f
from normalizacion import normalizar
from Cuartiles import Outliers

instancia = f.cargarInstancia(ruta='InstanciaClase.txt',delimiter='\t')
normalizar(instancia)


instancia2 = f.cargarInstancia2(ruta='InstanciaClase.txt',delimiter='\t')
Outliers(instancia2)
#print(instancia2)