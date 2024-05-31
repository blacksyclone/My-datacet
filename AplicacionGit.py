import pandas as pd
url= 'https://github.com/blacksyclone/My-datacet.git'

try:
    df= pd.read_csv(url)
    print("Primera filas del dataset:")
    print(df.head())
except Exception as e:
    print("Error al leer el dataset:", e)