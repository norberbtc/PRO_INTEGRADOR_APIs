import pandas as pd
import requests

def descargar_datos_csv(url):
    # Realiza un GET request a la URL
    response = requests.get(url)

    # Verifica el código de estado de la respuesta
    if response.status_code != 200:
        raise Exception(f"Error al descargar los datos: {response.status_code}")

    # Abre un archivo de texto plano con la extensión CSV
    with open("datos.csv", "w") as archivo:
        # Escribe la respuesta en el archivo
        archivo.write(response.text)

def procesar_datos(dataframe):
    # Verificar valores faltantes
    if dataframe.isnull().values.any():
        dataframe = dataframe.dropna()
        print("Se eliminaron valores faltantes.")

    # Verificar filas repetidas
    if dataframe.duplicated().any():
        dataframe = dataframe.drop_duplicates()
        print("Se eliminaron filas duplicadas.")

    # Verificar y eliminar valores atípicos
    # (Implementa aquí la lógica para detectar y eliminar valores atípicos)

    # Crear columna de categoría por edades
    bins = [0, 12, 19, 39, 59, float('inf')]
    labels = ['Niño', 'Adolescente', 'Joven adulto', 'Adulto', 'Adulto mayor']
    dataframe['Edad_Categoria'] = pd.cut(dataframe['Edad'], bins=bins, labels=labels)

    # Guardar el resultado como CSV
    dataframe.to_csv("datos_procesados.csv", index=False)
    print("Datos procesados y guardados como 'datos_procesados.csv'.")

def main():
    # Descargar datos CSV
    descargar_datos_csv("https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv")

    # Cargar datos en un DataFrame
    df = pd.read_csv("datos.csv")

    # Procesar datos
    procesar_datos(df)

if __name__ == "__main__":
    main()
