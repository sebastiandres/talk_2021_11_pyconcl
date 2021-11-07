import streamlit as st
import importlib
import glob

# Parameters
STARTING_SLIDE = 0
repo_path = "https://raw.githubusercontent.com/sebastiandres/talk_2021_11_pyconcl/main/images"

# Config and setup
st.set_page_config(layout="wide", page_title="Pycon Chile 2021", initial_sidebar_state="collapsed")
slide_files = sorted(glob.glob("slides/slide_*.py"))
N = len(slide_files)
if 'slide_number' not in st.session_state:
	st.session_state.slide_number = STARTING_SLIDE

# Upper menu
st.sidebar.write("Slide:")
c1, c2, c3 = st.sidebar.columns([.3, .3, .5])
c1.write("")
c1.write("")
if c1.button("<") and st.session_state.slide_number>0:
    st.session_state.slide_number -= 1
c3.write("")
c3.write("")
if c3.button(">") and st.session_state.slide_number<N-1:
    st.session_state.slide_number += 1

slide = c2.text_input("\b", value=f"{st.session_state.slide_number}")
st.session_state.slide_number = int(slide)
if st.session_state.slide_number>=1:
    st.markdown("Pycon Chile: **WebApps con Streamlit : ¡más fácil que la tabla del uno, poh!**")
if st.session_state.slide_number>=2:
    st.markdown(f"Sebastián Flores, @sebastiandres ![]({repo_path}/github.png) ![]({repo_path}/twitter.png) ![]({repo_path}/linkedin.png) [sebastiandres.xyz](sebastiandres.xyz), Nov 2021.")
if st.session_state.slide_number==10:
    st.sidebar.write('Esto está en el sidebar')
    if st.sidebar.button('Mi botón opcional'):
        st.balloons()

# Display the slides
module_str = slide_files[st.session_state.slide_number].replace("/",".").replace(".py","")
current_slide = importlib.import_module(module_str)
current_slide.display()