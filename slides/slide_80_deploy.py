import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display():
    c1, c2 = st.columns([9,1])
    c1.title("¿Como se comparte online?")
    show_code = c2.checkbox("Código")
    with st.echo("below") if show_code else skip_echo():
        st.write("Puedes desplegar la aplicación por tu cuenta, por ejemplo en heroku o digital ocean.")
        st.write("Streamlit ofrece distintos planes para desplegar la app.")        
        st.write("El plan gratuito permite tener 3 apps gratuitas.")                