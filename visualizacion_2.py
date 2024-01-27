import matplotlib.pyplot as plt
import pandas as pd
# Crear subplots para las gráficas de torta
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Cantidad de anémicos
anemia_counts = df['anaemia'].value_counts()
axs[0, 0].pie(anemia_counts, labels=['No Anémicos', 'Anémicos'], autopct='%1.1f%%', colors=['skyblue', 'lightcoral'])
axs[0, 0].set_title('Distribución de Anémicos')

# Cantidad de diabéticos
diabetes_counts = df['diabetes'].value_counts()
axs[0, 1].pie(diabetes_counts, labels=['No Diabéticos', 'Diabéticos'], autopct='%1.1f%%', colors=['skyblue', 'lightcoral'])
axs[0, 1].set_title('Distribución de Diabéticos')

# Cantidad de fumadores
smoking_counts = df['smoking'].value_counts()
axs[1, 0].pie(smoking_counts, labels=['No Fumadores', 'Fumadores'], autopct='%1.1f%%', colors=['skyblue', 'lightcoral'])
axs[1, 0].set_title('Distribución de Fumadores')

# Cantidad de muertos
death_counts = df['DEATH_EVENT'].value_counts()
axs[1, 1].pie(death_counts, labels=['No Muertos', 'Muertos'], autopct='%1.1f%%', colors=['skyblue', 'lightcoral'])
axs[1, 1].set_title('Distribución de Muertos')

# Ajustes finales
plt.tight_layout()
plt.show()
