import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display():
    c1, c2 = st.columns([9,1])
    show_code = c2.checkbox("Código")
    with st.echo("below") if show_code else skip_echo():
        #No olvidar importar streamlit como st
        repo_path = "https://raw.githubusercontent.com/sebastiandres/talk_2021_11_pyconcl/main/images"
        st.markdown("## Pycon Chile")
        st.markdown("# WebApps con Streamlit: ¡más fácil que la tabla del uno, poh!")
        st.markdown("## Sebastián Flores, Noviembre 2021")
        st.markdown("#### Presentación realizada en streamlit *(Streamlit-ception)*")
        # Solo python, nada de html o css por acá...
   