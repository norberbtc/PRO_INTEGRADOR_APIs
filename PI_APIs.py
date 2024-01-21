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

# Uso del codigo 
descargar_datos_csv("https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv")
