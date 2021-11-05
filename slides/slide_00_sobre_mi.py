import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display():
    c1, c2 = st.columns([9,1])
    c1.title("Sobre mí")
    show_code = c2.checkbox("Código")
    with st.echo("below") if show_code else skip_echo():
        # No olvidar importar streamlit como st
        repo_path = "https://raw.githubusercontent.com/sebastiandres/talk_2021_11_pyconcl/main/images"
        # Streamlit, por favor, dame 2 columnas de anchos relativos 3 y 7
        c1, c2 = st.columns([3, 7])
        # Contenido de la primera columna
        c1.image('images/avatar.jpeg', width=300)
        # Contenido de la segunda
        c2.markdown("## Sebastián Flores")
        c2.markdown("### Chief Data Officer en uPlanner - Data-Driven Solutions for Education")
        c2.markdown("#### PyCon: 2020 (🇨🇴, 🇦🇷) y 2021 (🌎, 🇦🇷, 🇨🇱)")
        c2.markdown("#### Blog: [sebastiandres.xyz](https://sebastiandres.xyz)")
        c2.markdown(f"#### @sebastiandres en ![]({repo_path}/github.png) ![]({repo_path}/twitter.png) ![]({repo_path}/linkedin.png)")
        # Solo python, nada de html o css por acá...

