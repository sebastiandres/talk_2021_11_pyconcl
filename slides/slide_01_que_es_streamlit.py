import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display():
    c1, c2 = st.columns([9,1])
    c1.title("¿Qué es streamlit?")
    show_code = c2.checkbox("Código")

    with st.echo("above") if show_code else skip_echo():
        st.markdown('### _"Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few minutes you can build and deploy powerful data apps."_')
        st.markdown("Streamlit recientemente cumplió 2 años y sacó su release 1.1.0, con un versionamiento *vertiginoso*.")
        st.markdown("Es muchísimo más simple de usar que frameworks para la web como django, flask, bottle u otras. ¡Todo es python!")
        st.markdown("En el nicho de dashboard y webapps es comparable a las librerías: Jupyter notebook, Dash - Plotly, Holoviz Panel y Gradio")
        st.image("images/comparacion.png")

