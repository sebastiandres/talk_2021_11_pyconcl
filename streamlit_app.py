import streamlit as st
import importlib

# Set wide display
st.set_page_config(layout="wide")

# Upper menu
c1, c2, c3 = st.columns([0.1, 0.8, 0.1])
c1.markdown("QR")
c2.write("Pycon Chile - Noviembre 2021") 
c2.markdown("Created by [sebastiandres](https://sebastiandres.xyz)") 
raw_slide_number = c3.number_input("", min_value=0, max_value=3, step=1)
slide_number = int(raw_slide_number)

# Display the slides
module_str = f"slides.slide_{slide_number:02d}"
current_slide = importlib.import_module(module_str)
current_slide.display()