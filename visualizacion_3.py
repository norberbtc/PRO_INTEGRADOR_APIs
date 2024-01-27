import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
import plotly.express as px

# Eliminar columnas 'DEATH_EVENT' y 'categoria_edad'
X = df.drop(columns=['DEATH_EVENT', 'categoria_edad']).values

# Exportar un array unidimensional de la columna 'DEATH_EVENT'
y = df['DEATH_EVENT'].values

# Realizar reducción de dimensionalidad con t-SNE
X_embedded = TSNE(n_components=3, learning_rate='auto', init='random', perplexity=3).fit_transform(X)

# Crear DataFrame con los datos reducidos y la columna 'DEATH_EVENT'
df_embedded = pd.DataFrame(X_embedded, columns=['Dim1', 'Dim2', 'Dim3'])
df_embedded['DEATH_EVENT'] = y

# Crear gráfico de dispersión 3D con Plotly
fig = px.scatter_3d(
    df_embedded,
    x='Dim1',
    y='Dim2',
    z='Dim3',
    color='DEATH_EVENT',
    title='Gráfico de Dispersión 3D - Reducción t-SNE',
    labels={'Dim1': 'Dimensión 1', 'Dim2': 'Dimensión 2', 'Dim3': 'Dimensión 3'},
    color_discrete_map={0: 'blue', 1: 'red'}  # Colores para las clases (0: Vivo, 1: Muerto)
)

# Mostrar el gráfico
fig.show()
