import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display():
    c1, c2 = st.columns([9,1])
    c1.title("Un ejemplo simple")
    show_code = c2.checkbox("Código")

    with st.echo("above") if show_code else skip_echo():
        c1, c2 = st.columns([4, 6])
        # Columna izquierda
        with c1:
            st.image("images/ejemplo_simple.png")
        # Columna derecha
        with c2:
            st.markdown("## Pregunta #1")
            st.markdown("### ¿Cómo harían una página web que:")
            st.markdown(f"#### {'&nbsp;'*5} permitiera cargar una foto, ")
            st.markdown(f"#### {'&nbsp;'*10}  la convirtiera a escala de grises, ")
            st.markdown(f"#### {'&nbsp;'*15}  mostrara la imagen resultante,")
            st.markdown(f"#### {'&nbsp;'*20}  y permitiera descargarla?")
            st.markdown("")
            st.markdown("## Pregunta #2")
            st.markdown("#### ¿Cuántas líneas de código creen que debería tomar eso?")
