import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display():
    c1, c2 = st.columns([9,1])
    c1.title("¡Gracias!")
    show_code = c2.checkbox("Código")
    with st.echo("below") if show_code else skip_echo():
        c1, c2 = st.columns([6, 4])
        c1.image("images/encuestador.jpg")
        c1.write("Espero la charla los inspire para comenzar a usar streamlit en sus proyectos.")
        c1.write("QR")
