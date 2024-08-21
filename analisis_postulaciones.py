import pandas as pd
def transformar_a_csv():
    # Ruta al archivo Excel
    archivo_excel = 'PostulaciónySelección_Admisión2024/Libro_CódigosADM2024_ArchivoD.xlsx'

    # Leer todas las hojas del archivo Excel en un diccionario de DataFrames
    hojas = pd.read_excel(archivo_excel, sheet_name=None, engine='openpyxl')

    # Iterar sobre el diccionario y guardar cada hoja en un archivo CSV
    for nombre_hoja, df in hojas.items():
        archivo_csv = f'PostulaciónySelección_Admisión2024/Libro_CódigosADM2024_ArchivoD_{nombre_hoja}.csv'  # Ruta al archivo CSV, usando el nombre de la hoja
        df.to_csv(archivo_csv, index=False)  # Guardar el DataFrame en un archivo CSV
        print(f"Datos de la hoja '{nombre_hoja}' guardados en {archivo_csv}")

import os

dir=os.listdir()
for a in dir:
    if os.
print(dir)