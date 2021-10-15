import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display():
    c1, c2 = st.columns([9,1])
    c1.title("¿Como funciona streamlit?")
    show_code = c2.checkbox("Mostrar código")

    with st.echo("above") if show_code else skip_echo():
        c1, c2 = st.columns([6, 4])
        c1.markdown("Programar con streamlit es como jugar con legos...")
        c1.markdown("...")
        c2.image("images/lego.jpg")
        c2.caption("https://www.reddit.com/r/chile/comments/mkbzx2/santiago_en_lego/")
