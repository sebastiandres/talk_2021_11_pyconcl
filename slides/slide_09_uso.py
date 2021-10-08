import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display(my_title = "", show_code=False):
    with st.echo("below") if show_code else skip_echo():
        st.title("¿Cómo se usa?")
        st.write("Típicamente se edita un archivo `streamlit_app.py`")
        st.write("Y luego se ejecuta en el terminal:")
        st.write("`steamlit run streamlit_app.py`")
        st.code("steamlit run streamlit_app.py")
