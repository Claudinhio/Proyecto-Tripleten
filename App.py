#Importar librerias pandas, plotly.express y streamlit

import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV del conjunto de datos en un DataFrame
car_data = pd.read_csv('/Users/claudio.merino/Documents/nuevo_directorio1/proyecto_1/vehicles_us.csv')

# Encabezado de la aplicación
st.header('Aplicación de Cuadro de Mandos para Datos de Vehículos')

# Casilla de verificación para construir un histograma
build_histogram = st.checkbox('Construir un Histograma')

if build_histogram:
    # Mensaje
    st.write('Construir un histograma para la columna odómetro')
    
    # Construir el histograma
    fig_histogram = px.histogram(car_data, x="odometer")
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_histogram, use_container_width=True)

# Casilla de verificación para construir un gráfico de dispersión
build_scatter = st.checkbox('Construir un Gráfico de Dispersión')

if build_scatter:
    # Mensaje
    st.write('Construir un gráfico de dispersión para las columnas año y precio')
    
    # Construir el gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="year", y="price", color="fuel")
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
