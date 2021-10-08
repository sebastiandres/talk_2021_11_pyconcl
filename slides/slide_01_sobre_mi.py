import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display(my_title = "", show_code=False):
    with st.echo("below") if show_code else skip_echo():
        st.title("Sobre mí")
        c1, c2 = st.columns([0.3, 0.7])
        c1.image('images/avatar.jpeg', width=300)
        c2.write("## Sebastián Flores")
        c2.markdown("## [![F](https://img.shields.io/twitter/follow/sebastiandres?style=social)](https://www.twitter.com/sebastiandres)")
        c2.markdown("## [sebastiandres.xyz](https://sebastiandres.xyz)")
        c2.markdown("### Pycon Colombia [1], Argentina [2], Latam [1], Chile [1]")

