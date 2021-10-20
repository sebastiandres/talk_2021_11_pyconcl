import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display():
    c1, c2 = st.columns([9,1])
    c1.title("¿Donde vive streamlit?")
    show_code = c2.checkbox("Código")

    with st.echo("above") if show_code else skip_echo():
        st.markdown("Además de librerías web (django, flask), en el nicho de dashboard y webapps son comunes las siguientes librerías:")
        st.markdown("* Dash - Plotly\n* Holoviz Panel\n* Gradio\n* Streamlit")
        st.image("images/comparacion.png")
        st.markdown("Streamlit recientemente cumplió 2 años y sacó su release 1.0.0")

