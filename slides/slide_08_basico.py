import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display():

    c1, c2 = st.columns([9,1])
    c1.title("Elementos Básicos de Streamlit")
    show_code = c2.checkbox("Mostrar código")

    st.markdown("---")
    with st.echo("below") if show_code else skip_echo():
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.button("Mi botón")
        c2.checkbox("Un Checkbox")
        c3.number_input("Input de número")
        c4.slider("Slider numérico", min_value=0, max_value=100)
        c5.metric("Pycon Chile", "#1")
    
    st.markdown("---")
    with st.echo("below") if show_code else skip_echo():
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.text_input("Input de texto")
        c2.select_slider("Slider de Texto", options=["uno", "dos", "tres", "cuatro"])
        c3.radio("Radio", options=["AM", "FM", "Online"])
        c4.selectbox("¿Comida chilena?", options=["Sopaipilla", "Terremoto", "Mote con Huesillo", "Pastel de Choclo"])
        c5.multiselect("Tocomple", options=["Tomate", "Palta", "Mayo", "Mostaza", "Ketchup", "Piña"])

    st.markdown("---")
    with st.echo("below") if show_code else skip_echo():
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.download_button("Descargar archivo", data=b"0101", help="Una explicación al botón")
        c2.file_uploader("Cargar archivos")
        c3.color_picker("Seleccionar color")
        c4.date_input("Seleccionar fecha")  
        c5.time_input("Seleccionar hora")  

    st.markdown("---")
    with st.echo("below") if show_code else skip_echo():
        c1, c2, c3, c4 = st.columns(4)
        c1.error("Mensaje de error")
        c2.warning("Mensaje de warning")
        c3.info("Mensaje informativo")
        c4.success("Mensaje de éxito")

    st.markdown("---")
    with st.echo("below") if show_code else skip_echo():
        c1, c2, c3, c4 = st.columns(4)
        if c1.button("¡Bravo!"):
            st.balloons()
        if c2.button("Progreso"):
            import time
            my_bar = c2.progress(0)
            for i in range(0,101,10):
                my_bar.progress(i)
                time.sleep(.2)
            my_bar.empty()
        if c3.button("Mensaje dinámico"):
            import time
            with st.spinner('Desaparecerá en 1.5 segundos...'):
                time.sleep(1.5)
        if c4.button("Mensaje de Excepción"):
            try:
                1/0
            except Exception as e:
                st.exception(e)

