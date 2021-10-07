import streamlit as st
import pandas as pd
import numpy as np

def display(my_title = "", show_code=False):
    """Creates the custom content of a page.

    args:
    - my_title: string with the title for the page.
    """
    if my_title:
        st.title(my_title)
    # Write
    st.title("Slide 03 - My content")
    with st.echo('below'):
        st.write("This is EXTRAORDINARY") # Strings