import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display():
    c1, c2 = st.columns([9,1])
    c1.title("¿Como se comparte online?")
    show_code = c2.checkbox("Código")
    with st.echo("below") if show_code else skip_echo():
        st.write("**Prerrequisito:** Almacenar en un repositorio con git.")
        with st.expander("Streamlit Cloud"):
            c11, c12 = st.columns(2)
            c11.subheader("Streamlit Cloud")
            c11.write("Múltiples opciones: gratis y de pago")
            c11.write("Permite vincular a repositorio de github y hacer deploy en 1 click")
            c11.write("¡La página web se actualiza automática al cambiar el código en el repositorio!")
            c11.write("La opción gratis permite tener hasta 3 apps en línea.")
            c12.video("videos/streamlit_sharing_silent.mp4")

        with st.expander("Hugging Face"):
            st.subheader("Deploy en Spaces de Hugging Face")
            c11, c12 = st.columns(2)
            c11.write("(1) Crear cuenta e ir a https://huggingface.co/docs/hub/spaces")
            c11.write("(2) Crear un espacio de tipo streamlit")
            c11.write("(3) Crear o cargar los archivos necesarios: `requirements.txt` y `app.py`")
            c11.write("Tutorial: [link](https://huggingface.co/blog/streamlit-spaces)")
            c12.video("videos/hugging_face.mp4")

        with st.expander("Google Colab"):
            st.subheader("Google Colab")
            st.write("Puedes usar un notebook de Google Colab para lanzar streamlit, usando el siguiente contenido en las celdas:")
            st.code("!git clone https://github.com/USER_NAME/REPO_NAME.git")
            st.code("cd REPO_NAME")
            st.code("!pip install -r requirements.txt")
            st.code("!pip install pyngrok")
            st.code("""from pyngrok import ngrok
public_url = ngrok.connect(port='80')
print('Link to web app:', public_url)
""")
            st.write("Debería entregar un texto como el siguiente")
            st.text('Link to web app: NgrokTunnel: "http://3728-35-229-174-231.ngrok.io" -> "http://localhost:80"')
            st.code("!streamlit run --server.port 80 app.py >/dev/null")
            st.write("La página web está disponible en la dirección de ngrok.io, pero sólo mientras está activa la sesión de Google Colab.")
            st.write("Es gratis, pero inestable y no lo más cómodo para desarrollar.")

        with st.expander("Autogestionado"):
            st.subheader("Autogestionado")
            st.write("Siempre es posible desplegar la aplicación por tu cuenta.")
            st.write("Algunass alternativas son, por ejemplo en Heroku o Digital Ocean (entre otros).")
            st.write("Heroku: [link](https://towardsdatascience.com/deploying-a-basic-streamlit-app-to-heroku-be25a527fcb3)")
            st.write("Digital Ocean: 404")