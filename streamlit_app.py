import streamlit as st
import importlib
import glob

# Config and setup
st.set_page_config(layout="wide")
slide_files = sorted(glob.glob("slides/slide_*.py"))
N = len(slide_files)
if 'slide_number' not in st.session_state:
	st.session_state.slide_number = 0

# Upper menu
L, c1, c2, c3 = st.columns([8, .5, .5, 0.5])
st.markdown("---")
if c1.button("<") and st.session_state.slide_number>0:
    st.session_state.slide_number -= 1
if c3.button(">") and st.session_state.slide_number<N-1:
    st.session_state.slide_number += 1
c2.write(f"{st.session_state.slide_number}") # Put it after the buttons, so it gets updated accordingly
if st.session_state.slide_number>=2:
    L.markdown("###### **WebApps con Streamlit : ¡más fácil que la tabla del uno, poh!**")
    L.markdown("###### Pycon Chile, Noviembre 2021, por Sebastián Flores [^T^L]/[@sebastiandres](https://github.com/sebastiandres) (GH, TW, LI) | [sebastiandres.xyz](sebastiandres.xyz)")
# https://img.shields.io/badge/-FFFFFF?logo=twitter
# https://img.shields.io/badge/-FFFFFF?logo=github
# https://img.shields.io/badge/-FFFFFF?logo=linkedin


# Display the slides
module_str = slide_files[st.session_state.slide_number].replace("/",".").replace(".py","")
current_slide = importlib.import_module(module_str)
current_slide.display()
