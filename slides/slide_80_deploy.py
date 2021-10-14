import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display(my_title = "", show_code=False):
    with st.echo("below") if show_code else skip_echo():
        st.title("¿Como se comparte online?")
        st.write("Puedes desplegar la aplicación por tu cuenta, por ejemplo en heroku o digital ocean.")
        st.write("Streamlit ofrece distintos planes para desplegar la app.")        
        st.write("El plan gratuito permite tener 3 apps gratuitas.")                