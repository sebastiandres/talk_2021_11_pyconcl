import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display():
    _, c1, c2, _ = st.columns([2,7,3,2])
    with c1:
        repo_path = "https://raw.githubusercontent.com/sebastiandres/talk_2021_11_pyconcl/main/images"
        st.markdown("## Pycon Chile")
        st.markdown("# WebApps con Streamlit:")
        st.markdown("#    _¡más fácil que la tabla del uno, poh!_")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("## Sebastián Flores, Noviembre 2021")
        st.markdown("##### Presentación realizada en streamlit (:exploding_head: *streamlit-ception*)")
        st.write("Repositorio de la presentación: https://github.com/sebastiandres/talk_2021_11_pyconcl")

    with c2:
        st.image("images/streamlit_cl.png")