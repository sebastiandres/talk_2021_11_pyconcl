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
c1, c2, c3, c4 = st.columns([12, 1, 1, 1])
c1.markdown("###### Pycon Chile, Noviembre 2021.")
c1.markdown("###### **WebApps con Streamlit: ¡más fácil que la tabla del uno, poh!**")
show_code = c1.checkbox("Mostrar código")
#c1.markdown("###### Hecho en [![this is an image link](https://i.imgur.com/iIOA6kU.png)](https://www.streamlit.io/)&nbsp, with :heart: by [@sebastiandres](https://sebastiandres.xyz) &nbsp | &nbsp [![F](https://img.shields.io/twitter/follow/sebastiandres?style=social)](https://www.twitter.com/sebastiandres)")
if c2.button("<") and st.session_state.slide_number>0:
    st.session_state.slide_number -= 1
if c4.button(">") and st.session_state.slide_number<N-1:
    st.session_state.slide_number += 1
c3.write(f"{st.session_state.slide_number}") # Put it after the buttons, so it gets updated accordingly
st.markdown("---")

# Display the slides
module_str = slide_files[st.session_state.slide_number].replace("/",".").replace(".py","")
print(module_str)
current_slide = importlib.import_module(module_str)
current_slide.display(show_code=show_code)
#from slides import slide_00
#slide_00.display(show_code=show_code)