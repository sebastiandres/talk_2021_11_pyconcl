import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display():
    t, cb = st.columns([9,1])
    t.title("Ejemplo 1 - Web app simple")
    show_code = cb.checkbox("Código")

    with st.echo("above") if show_code else skip_echo():

        import os

        # Define the function
        def processing_function(image_filepath):
            """
            Converts to gray scale
            """
            grey_image_filepath = image_filepath.replace(".", "_grey.")
            st.write(grey_image_filepath)
            os.system("cp {image_filepath} {grey_image_filepath}")
            return grey_image_filepath

        # Layout
        c1, c2, c3, c4, c5 = st.columns([2,1,2,1,2])

        # Carga
        with c1:
            uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg'])

        # Procesamiento
        if uploaded_file is not None:
            with c2:
                c2.write(">")
                uploaded_filename = uploaded_file.name
                file_details = {"FileName":uploaded_file.name, "FileType":uploaded_file.type,"FileSize":uploaded_file.size}
                st.write(file_details)
                processed_file = processing_function(uploaded_filename)
 
        # Descarga
        if uploaded_file is not None:
            c4.write(">")
            with open(processed_file, "rb") as file_content:
               c5.download_button(label="Descarga", data=file_content, file_name=processed_file, mime="jpeg")