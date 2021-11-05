import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display():
    c1, c2 = st.columns([9,1])
    c1.title("¡Gracias!")
    show_code = c2.checkbox("Código")
    with st.echo("below") if show_code else skip_echo():
        _, c1, _, c2, _ = st.columns([2, 6, 2, 4, 2])
        c1.image("images/encuestador.jpg")
        c2.image("images/qr.png", caption="https://bit.ly/3k4ckir")
        st.write("### ¡Espero la charla los motive a usar streamlit en sus proyectos!")
        st.write("### ¡Bienvenidos a streamlit!")
        st.write("Repositorio de la presentación: https://github.com/sebastiandres/talk_2021_11_pyconcl")
        