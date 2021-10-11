import streamlit as st
import pandas as pd
import numpy as np

#from code.shared_functions import skip_echo
#from code.shared_functions import documentation

def display():
    st.title("Elementos en Streamlit")
    st.markdown("---")
    c1, c2, c3, c4, c5 = st.columns(5)
    #c1.code("c1.error")
    c1.error("Mensaje de error")
    #c2.code("Mensaje de warning")
    c2.warning("Mensaje de warning")
    #c3.code("Mensaje informativo")
    c3.info("Mensaje informativo")
    #c4.code("Mensaje de excepción")
    #try:
    #    1/0
    #except ValueError:
    #    c4.exception("Mensaje de excepción")
    #c5.code("Mensaje de éxito")
    c5.success("Mensaje de éxito")

    st.markdown("---")
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Pycon", "#1")

    st.markdown("---")
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    c1.button("Mi botón")
    c2.checkbox("Un Checkbox")
    c3.text_input("Input de texto")
    c4.number_input("Input de número")
    c5.slider("Input de número", min_value=0, max_value=100)

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    c1.select_slider("Slider", options=["uno", "dos", "tres", "cuatro"])
    c2.radio("Radio", options=["radio", "tv"])
    c3.multiselect("Multiselect", options=["radio", "tv"])

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    if c1.button("Globos"):
        st.balloons()
    if c2.button("Barra progreso"):
        import time
        my_bar = c2.progress(0)
        for i in range(0,101,10):
            my_bar.progress(i)
            time.sleep(.2)
        my_bar.empty()
    if c3.button("Spinner?"):
        import time
        with st.spinner('Desaparecerá en 1.5 segundos...'):
            time.sleep(1.5)
        #c3.success('Done')            

    st.markdown("---")
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.button("Botónazo")
    c1.download_button("Botón descarga", data=b"0101", help="Una explicación al botón")
    #c3.markdown("File uploader")
    c2.file_uploader("Carga de archivos")
    #c4.markdown("Button")
    c3.color_picker("Seleccionador el color")
    #c5.markdown("Button")
    c4.date_input("Selecciona la fecha")  
    c5.time_input("Selecciona la hora")  

    #c1.markdown("Button")
    #c1.button("Botón", help="Una explicación al botón")

