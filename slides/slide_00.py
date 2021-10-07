import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display(my_title = "", show_code=False):
    """Creates the custom content of a page.

    args:
    - my_title: string with the title for the page.
    """
    if my_title:
        st.title(my_title)
    # Write
    st.title("Slide 00 - My content")
    with st.echo("below") if show_code else skip_echo():
        st.write("This is a \n string") # Strings
