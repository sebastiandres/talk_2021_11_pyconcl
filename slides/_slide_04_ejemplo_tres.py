import streamlit as st
import pandas as pd
import numpy as np
import cv2

from code.shared_functions import skip_echo

def display(my_title = "", show_code=False):
    with st.echo("below") if show_code else skip_echo():
        c1, c2 = st.columns([10,1])
        c1.title("Ejemplo 3 - ?")
        show_code = c2.checkbox("Código")
        st.caption("Webapp de XYZ - http://www.github.com/XYZ")
        with st.echo("above") if show_code else skip_echo():

            import os
            import numpy as np
            from tensorflow.keras.models import load_model
            from streamlit_drawable_canvas import st_canvas

            model = load_model('model')

            st.markdown("Dibuja un dígito")

            c1, c2, c3 = st.columns([3,3,3])

            with c1:
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

            if c2.button("Resize"):
                img = cv2.resize(canvas_result.image_data.astype('uint8'), (28, 28))
                rescaled = cv2.resize(img, (SIZE, SIZE), interpolation=cv2.INTER_NEAREST)
                c2.write('Model Input')
                c2.image(rescaled)

            if c3.button("Predict"):       
                img = cv2.resize(canvas_result.image_data.astype('uint8'), (28, 28))
                rescaled = cv2.resize(img, (SIZE, SIZE), interpolation=cv2.INTER_NEAREST)
                c2.write('Model Input')
                c2.image(rescaled)
                test_x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                val = model.predict(test_x.reshape(1, 28, 28))
                c3.write(f'result: {np.argmax(val[0])}')
                c3.bar_chart(val[0])


if __name__=="__main__":
    display()                