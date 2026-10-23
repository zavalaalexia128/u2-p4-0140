import pandas as pd
import numpy as np
# Zavala Medina| NC= 0150 |23 de Octubre de 2026
n_filas=5
n_columnas=5
tag_columnas=tuple("ABCDE") # etiquetas para las columnas
print(tag_columnas)
matriz=np.random.randint(1, 6, size=(n_filas,n_columnas))
print("Genera matriz de 5 filas por 5 columnas")
print("con numeros aleatorios comprendidos entre 1 y 10")
print(matriz)
# la variable df es DataFrame
df= pd.DataFrame(matriz, columns= tag_columnas)
print(" --- La tabla o DataFrame --- 0150")
print(df)
print("Zavala Medina| NC= 0150 |23 de Octubre de 2026")