import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display():
    c1, c2 = st.columns([9,1])
    c1.title("¿Qué es streamlit?")
    show_code = c2.checkbox("Código")

    with st.echo("above") if show_code else skip_echo():
        c1, c2 = st.columns([6,4])
        # Columna izquierda
        c1.markdown('### _"Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few minutes you can build and deploy powerful data apps."_')
        c1.markdown("Streamlit recientemente cumplió 2 años y sacó su release 1.1.0, con un versionamiento *vertiginoso*.")
        c1.markdown("Es muchísimo más simple de usar que frameworks para la web como django, flask, bottle u otras. ¡Todo es python!")
        c1.markdown("En el nicho de dashboard y webapps se relaciona con las librerías: plotly, panel, voila y gradio.")
        c1.markdown("Personalmente, antes de conocer streamlit usaba jupyter notebooks como _wrapper_ de código.")
        # Columna derecha
        image=c2.selectbox("Imagen", options=["Github Stars", "Github Commits", "Github Pull Requests"])
        c2.image(f"images/{image.replace(' ','_')}.png", caption="https://vesoft-inc.github.io/github-statistics/")

