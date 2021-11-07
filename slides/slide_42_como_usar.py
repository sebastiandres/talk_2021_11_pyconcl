import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display():
    c1, c2 = st.columns([9,1])
    c1.title("¿Cómo se usa?")
    show_code = c2.checkbox("Código")
    with st.echo("above") if show_code else skip_echo():
        st.write("**(1)** Crear y editar un archivo `streamlit_app.py` con algún contenido:")
        st.code("""import streamlit as st
# Sidebar
st.sidebar.markdown("Creado por ...")
# Main content
st.title("Mi Primera App en :streamlit:")
""")
        st.write("**(2)** Mantener actualizado el archivo `requirements.txt` con las librerías a utilizar:")
        st.code("""streamlit==1.1.0
watchdog""")
        st.write("**(3)** Es recomendable instalar en un ambiente virtual:")
        st.code("""virtualenv venv\nsource venv/bin/activate\npip install -r requirements.txt""")
        st.write("**(4)** Ejecutar en el terminal:")
        st.code("$ streamlit run streamlit_app.py")
        st.write("¡Lo anterior abrirá en el navegador la página web creada!")
        st.write("**(5)** Editar el archivo `streamlit_app.py` y verificar los cambios en el navegador.")
