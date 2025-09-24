import streamlit as st 
import pandas as pd

def mostrar_exploracion_datos():
    st.sidebar.info("Explora y analiza los datos disponibles en el sistema.")
    st.title("Exploración de Datos 📊")
    st.write("Aquí puedes explorar los datos disponibles.")
    try:
        datos = pd.read_csv('datos_exploracion.csv')
        st.dataframe(datos)
    except FileNotFoundError:
        st.warning("No se encontró el archivo 'datos_exploracion.csv'.")