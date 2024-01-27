import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv("datos.csv")

# Graficar la distribución de edades con un histograma
plt.figure(figsize=(10, 6))
plt.hist(df['age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Graficar histogramas agrupados por hombre y mujer
fig, axs = plt.subplots(3, 2, figsize=(14, 12))

# Cantidad de anémicos
axs[0, 0].bar(df['sex'], df[df['anaemia'] == 1]['sex'].count(), color='lightcoral', label='Anémicos', align='edge')
axs[0, 0].bar(df['sex'], df[df['anaemia'] == 0]['sex'].count(), color='skyblue', label='No Anémicos', align='edge')
axs[0, 0].set_title('Cantidad de Anémicos')
axs[0, 0].set_xlabel('Sexo')
axs[0, 0].set_ylabel('Cantidad')
axs[0, 0].legend()

# Cantidad de diabéticos
axs[0, 1].bar(df['sex'], df[df['diabetes'] == 1]['sex'].count(), color='lightcoral', label='Diabéticos', align='edge')
axs[0, 1].bar(df['sex'], df[df['diabetes'] == 0]['sex'].count(), color='skyblue', label='No Diabéticos', align='edge')
axs[0, 1].set_title('Cantidad de Diabéticos')
axs[0, 1].set_xlabel('Sexo')
axs[0, 1].set_ylabel('Cantidad')
axs[0, 1].legend()

# Cantidad de fumadores
axs[1, 0].bar(df['sex'], df[df['smoking'] == 1]['sex'].count(), color='lightcoral', label='Fumadores', align='edge')
axs[1, 0].bar(df['sex'], df[df['smoking'] == 0]['sex'].count(), color='skyblue', label='No Fumadores', align='edge')
axs[1, 0].set_title('Cantidad de Fumadores')
axs[1, 0].set_xlabel('Sexo')
axs[1, 0].set_ylabel('Cantidad')
axs[1, 0].legend()

# Cantidad de muertos
axs[1, 1].bar(df['sex'], df[df['DEATH_EVENT'] == 1]['sex'].count(), color='lightcoral', label='Muertos', align='edge')
axs[1, 1].bar(df['sex'], df[df['DEATH_EVENT'] == 0]['sex'].count(), color='skyblue', label='No Muertos', align='edge')
axs[1, 1].set_title('Cantidad de Muertos')
axs[1, 1].set_xlabel('Sexo')
axs[1, 1].set_ylabel('Cantidad')
axs[1, 1].legend()

# Ajustes de diseño
for ax in axs.flat:
    ax.grid(True)

# Ajustes finales
plt.tight_layout()
plt.show()
