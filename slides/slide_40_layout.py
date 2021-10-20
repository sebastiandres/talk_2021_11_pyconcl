import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display():
    c1, c2 = st.columns([9,1])
    c1.title("¿Como organizo el contenido?")
    show_code = c2.checkbox("Código")
    with st.echo("below") if show_code else skip_echo():
        st.title("* Funcionamiento vertical")
        st.title("* Columnas")
        st.title("* Sidebar")
