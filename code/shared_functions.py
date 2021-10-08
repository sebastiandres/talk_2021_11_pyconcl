import streamlit as st

import contextlib

@contextlib.contextmanager
def skip_echo():
    yield None

def documentation(my_function):
    st.markdown(f"[API](https://docs.streamlit.io/en/stable/api.html#streamlit.{my_function})")
    return

'''
def what4(text):
    st.markdown("**What for?**: " + text)
    return

def examples():
    st.markdown("Examples:")
    return

def page_header(header):
    st.title(":sparkles: Streamlit Code Snippets :sparkles:")
    st.header(header)
    return

def breakline():
    st.markdown("---")
    return    

'''