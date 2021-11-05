import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

from code.shared_functions import skip_echo

def display():
    c1, c2 = st.columns([9,1])
    c1.title("Un ejemplo simple")
    show_code = c2.checkbox("Código")

    # Define the function
    # Inspiración: https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
    def processing_function(uploaded_file, R, B, G):
        """
        Converts to gray scale using R, B, G values
        """
        image_filepath = "tmp/" + uploaded_file.name
        grey_image_filepath = image_filepath.replace(".", "_grey.")
        with open(image_filepath, "wb") as f:
            f.write(uploaded_file.read())
        rgb = mpimg.imread(image_filepath)     
        gray = np.dot(rgb[...,:3], [R/100, G/100, B/100])
        plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(grey_image_filepath)        
        return image_filepath, grey_image_filepath

    with st.echo("above") if show_code else skip_echo():
        # ¡16 líneas de código!
        uploaded_file = st.file_uploader("Cargar imagen", type=['png'])
        if uploaded_file is not None:
            st.markdown("Selecciona perfil RGB (Red, Green, Blue):")
            c1, c2, c3 = st.columns(3)
            R = c1.slider("Red", min_value=0, max_value=100, value=30, step=5)
            G = c3.slider("Green", min_value=0, max_value=100, value=11, step=5)
            B = c2.slider("Blue", min_value=0, max_value=100, value=59, step=5)
            if st.button("Generar imagen en Blanco y Negro"):
                original_filepath, bw_filepath = processing_function(uploaded_file, R, B, G)
                c1, c2 = st.columns(2)
                c1.write("Imagen original")
                c1.image(original_filepath, width=200)
                c2.write("Imagen blanco y negro")
                c2.image(bw_filepath, width=200)
                with open(bw_filepath, "rb") as file_content:
                    c2.download_button(label="Descargar imagen", data=file_content, file_name="converted.png")