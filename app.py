import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
# Asegúrate de que el archivo esté en el directorio correcto
car_data = pd.read_csv('vehicles_us.csv')

# Títulos y encabezados
st.title('Análisis de Vehículos de Estados Unidos')
st.header('Visualización Interactiva de Datos')

# Botón para construir el histograma
if st.button('Construir histograma'):
    # Escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma con Plotly
    fig_hist = px.histogram(car_data,
                            x="odometer",
                            title="Distribución de Odómetro",
                            labels={"odometer": "Kilometraje",
                                    "price": "Precio"},
                            nbins=25)

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para construir el gráfico de dispersión
if st.button('Construir gráfico de dispersión'):
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para Kilometraje vs Precio')

    # Crear un gráfico de dispersión con Plotly
    fig_scatter = px.scatter(car_data,
                             x="odometer",
                             y="price",
                             title="Kilometraje vs Precio",
                             labels={"odometer": "Kilometraje", "price": "Precio"})

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)
