import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display():
    c11, c12 = st.columns([9,1])
    c11.title("¿Como organizar el contenido?")
    show_code = c12.checkbox("Código")
    with st.echo("above") if show_code else skip_echo():
        st.markdown("## Verticalidad")
        st.markdown("Los elementos de la página se van generando e insertando en el orden que se van leyendo en el archivo.")
        display_type = st.selectbox('Elegir tipo de display', ["Column","Expander"])
        c21, c22, c23 = st.columns(3)
        with c21 if display_type=="Column" else st.expander("Sidebar"):
            st.markdown("## Barra Lateral / Sidebar")
            st.image("images/sidebar.jpg", width=500)
            st.code("""# En lugar de llamar a st directamente
# Llamamos a st.sidebar
st.sidebar.write('Esto está en el sidebar')
if st.sidebar.button('Mi botón opcional'):
    st.balloons()
""")
        with c22 if display_type=="Column" else st.expander("Columns"):
            st.markdown("## Columns")
            st.image("images/columns.jpg", width=500)
            st.code("""
col1, col2 = st.columns(2) # Anchos iguales
#col1, col2 = st.columns([2, 1]) # Anchos proporcionales
with col1:
    st.write("A cat")
col2.write("A dog")
""")
        with c23 if display_type=="Column" else st.expander("Expander"):
            st.markdown("## Expander")
            st.image("images/expander.jpg", width=500)
            st.code("""with st.expander("Título del expander"):
    # Este contenido se muestra
    # solo cuando se expande el elemento
    st.write("Hola mundo")
""")