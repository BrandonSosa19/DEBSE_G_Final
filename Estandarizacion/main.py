import archivo as f
from normalizacion import normalizar
from estandarizacion import estandarizacion

instancia = f.cargarInstancia(ruta='Instancia_cancer.csv',delimiter=',')

estandarizacion(instancia)
# normalizar(instancia)
