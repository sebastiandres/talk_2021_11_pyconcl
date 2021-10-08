import streamlit as st
import importlib
import glob

# Config and setup
st.set_page_config(layout="wide")
slide_files = sorted(glob.glob("slides/slide_*.py"))
N = len(slide_files)
if 'slide_number' not in st.session_state:
	st.session_state.slide_number = 1

# Upper menu
L, c1, c2, c3, R = st.columns([8, .5, .5, 0.5, 1])
st.markdown("---")
if c1.button("<") and st.session_state.slide_number>0:
    st.session_state.slide_number -= 1
if c3.button(">") and st.session_state.slide_number<N-1:
    st.session_state.slide_number += 1
c2.write(f"{st.session_state.slide_number}") # Put it after the buttons, so it gets updated accordingly
if st.session_state.slide_number>0:
    L.markdown("###### Pycon Chile, Noviembre 2021.")
    L.markdown("###### **WebApps con Streamlit: ¡más fácil que la tabla del uno, poh!**")
    L.markdown("###### Sebastian Flores @sebastiandres")
    show_code = R.checkbox("Código")
else:
    show_code = False
# Display the slides
module_str = slide_files[st.session_state.slide_number].replace("/",".").replace(".py","")
current_slide = importlib.import_module(module_str)
current_slide.display(show_code=show_code)
