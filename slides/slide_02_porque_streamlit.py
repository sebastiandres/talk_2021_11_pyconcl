import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display():
    c1, c2 = st.columns([9,1])
    c1.title("¿Porqué usar streamlit?")
    show_code = c2.checkbox("Código")

    with st.echo("above") if show_code else skip_echo():
        c1, c2 = st.columns([5, 5])
        # Columna izquierda
        c1.markdown("")
        c1.markdown("")
        c1.markdown("### Fácil: ")
        c1.markdown("##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Elementos, variables, archivos, gráficos, etc: todo es Python :snake:")
        c1.markdown("### Simple pero potente: ")
        c1.markdown("##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Programar con streamlit es como jugar con legos... está diseñado para encajar perfectamente y que puedas armar todo lo que quieras.")
        c1.markdown("### Batteries included: ")
        c1.markdown("##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Incluye un sinfín de elementos de construcción, extensible mediante componentes, y por supuesto, todas tus librerías favoritas.")
        c1.markdown("")
        if c1.button("¡OK, me interesa!"):
            st.balloons()
        # Columna derecha
        c2.image("images/lego.jpg")
        c2.caption("https://www.reddit.com/r/chile/comments/mkbzx2/santiago_en_lego/")
