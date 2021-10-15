import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display():
    c1, c2 = st.columns([9,1])
    c1.title("Componentes de Streamlit")
    show_code = c2.checkbox("Mostrar código")
    st.caption("Basado en https://share.streamlit.io/napoles-uach/mundaneapps/main/st_parade.py")

    with st.echo("above") if show_code else skip_echo():

        import streamlit.components.v1 as components
        # Datos de opciones de páginas
        options = ["Documentación oficial",
                  "Tutorial",
                  "Ejemplo de componente"]
        descriptions = ["Documentación oficial de los componentess de Streamlit",
                       "Tutorial de Componentes de Streamlit, realizado por Fanilo Andrianasolo (@andfanilo)",
                       "Ejemplo de componente de captura de webcam"]
        urls = ["https://streamlit.io/components", 
                "https://streamlit-components-tutorial.netlify.app/",
                "https://share.streamlit.io/whitphx/streamlit-webrtc-example/main/app.py"]
        # Obtener la selección actual
        str_sel = st.selectbox("Selecciona contenido sobre Componentes", options)
        n_sel = options.index(str_sel)
        # Escribir descripción, url y desplegar contenido
        st.write(f"**Descripción**: {descriptions[n_sel]}")
        st.write(f"**url**: {urls[n_sel]}")
        st.write(f"**Contenido**:")
        components.iframe(urls[n_sel], height=800, scrolling=True)
        