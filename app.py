import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón

st.title('Análisis de Vehículos de Estados Unidos')
st.header('Histograma Interactivo')

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer",
                       title="Distribución de Odómetro",
                       labels={"odometer": "Kilometraje", "price": "Precio"},
                       nbins=25)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# boton para el grafico de dispersion
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('creacion de un grafico de dispersion')

    # creacion de un grafico de dispersion
    fig = px.scatter(car_data, x='odometer',
                     tittle='odometer vs precio',
                     labels={"odometer": "Kilometraje", "price": "Precio"})
