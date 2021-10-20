import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display():
    c1, c2 = st.columns([9,1])
    c1.title("¿Cómo se usa?")
    show_code = c2.checkbox("Código")
    with st.echo("above") if show_code else skip_echo():
        st.write("Típicamente se edita un archivo `streamlit_app.py`")
        st.write("Y luego se ejecuta en el terminal:")
        st.write("`streamlit run streamlit_app.py`")
        st.code("streamlit run streamlit_app.py")
