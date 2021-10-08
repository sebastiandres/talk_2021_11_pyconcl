import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display(show_code=False):
    with st.echo("below") if show_code else skip_echo():
        st.markdown("# Pycon Chile, Noviembre 2021")
        st.markdown("# WebApps con Streamlit: ¡más fácil que la tabla del uno, poh!")
        st.markdown("## Hecho en [![this is an image link](https://i.imgur.com/iIOA6kU.png)](https://www.streamlit.io/)")
        st.markdown("## Sebastián Flores - [![F](https://img.shields.io/twitter/follow/sebastiandres?style=social)](https://www.twitter.com/sebastiandres)")
        st.markdown("## [sebastiandres.xyz](https://sebastiandres.xyz)")
   