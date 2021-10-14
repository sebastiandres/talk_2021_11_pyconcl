import streamlit as st
import importlib
import glob

# Parameters
STARTING_SLIDE = 0

# Config and setup
st.set_page_config(layout="wide")
slide_files = sorted(glob.glob("slides/slide_*.py"))
N = len(slide_files)
if 'slide_number' not in st.session_state:
	st.session_state.slide_number = STARTING_SLIDE

# Upper menu
L, c1, c2, c3 = st.columns([8, .5, .5, 0.5])
#st.markdown("---")
if c1.button("<") and st.session_state.slide_number>0:
    st.session_state.slide_number -= 1
if c3.button(">") and st.session_state.slide_number<N-1:
    st.session_state.slide_number += 1
c2.write(f"{st.session_state.slide_number}") # Put it after the buttons, so it gets updated accordingly
if st.session_state.slide_number>=1:
    repo_path = "https://raw.githubusercontent.com/sebastiandres/talk_2021_11_pyconcl/main/images"
    L.markdown("Pycon Chile: **WebApps con Streamlit : ¡más fácil que la tabla del uno, poh!**")
if st.session_state.slide_number>=2:
    L.markdown(f"Sebastián Flores, @sebastiandres ![]({repo_path}/github.png) ![]({repo_path}/twitter.png) ![]({repo_path}/linkedin.png) [sebastiandres.xyz](sebastiandres.xyz), Nov 2021.")

# Display the slides
module_str = slide_files[st.session_state.slide_number].replace("/",".").replace(".py","")
current_slide = importlib.import_module(module_str)
current_slide.display()
