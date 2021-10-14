import streamlit as st
import pandas as pd
import numpy as np
import cv2

import os
import numpy as np
from tensorflow.keras.models import load_model
from streamlit_drawable_canvas import st_canvas

from code.shared_functions import skip_echo

#@st.cache 
def load_digits_model():
    model = load_model('model')
    return model

def display(my_title = "", show_code=False):
    with st.echo("below") if show_code else skip_echo():
        c1, c2 = st.columns([10,1])
        c1.title("Ejemplo 3 - ?")
        show_code = c2.checkbox("Código")
        st.caption("Webapp de XYZ - http://www.github.com/XYZ")
        with st.echo("above") if show_code else skip_echo():

            model = load_digits_model()

            c1, c2 = st.columns([3,6])

            with c1:
                st.markdown("Dibuja un dígito")
                SIZE = 28*10
                canvas_result = st_canvas(
                    fill_color='#000000',
                    stroke_width=20,
                    stroke_color='#FFFFFF',
                    background_color='#000000',
                    width=SIZE,
                    height=SIZE,
                    drawing_mode="freedraw", #if mode else "transform",
                    display_toolbar=True,
                    key='canvas')

            if c1.button("Reconocer dígito"):       
                img = cv2.resize(canvas_result.image_data.astype('uint8'), (28, 28))
                #rescaled = cv2.resize(img, (SIZE, SIZE), interpolation=cv2.INTER_NEAREST)
                #c2.write('Model Input')
                #c2.image(rescaled)
                c2.image(img)
                test_x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                val = model.predict(test_x.reshape(1, 28, 28))
                c2.write(f'Predicción: {np.argmax(val[0])}')
                c2.bar_chart(val[0])


if __name__=="__main__":
    display()                