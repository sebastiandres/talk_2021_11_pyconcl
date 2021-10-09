import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display(my_title = "", show_code=False):
    with st.echo("below") if show_code else skip_echo():
        st.title("¿Cómo funciona?")
        c1, c2 = st.columns([6, 4])
        c1.markdown("Programar con streamlit es como jugar con legos...")
        # https://www.reddit.com/r/chile/comments/mkbzx2/santiago_en_lego/
        c2.image("images/lego.jpg")
        c2.caption("https://www.reddit.com/r/chile/comments/mkbzx2/santiago_en_lego/")
