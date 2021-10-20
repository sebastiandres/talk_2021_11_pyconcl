import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

from code.shared_functions import skip_echo

def display():
    c1, c2 = st.columns([9,1])
    c1.title("Ejemplo 1 - Animación")
    show_code = c2.checkbox("Código")

    with st.echo("above") if show_code else skip_echo():

        def mi_funcion(x, i):
            return np.sin(x+0.1*i)

        def animate(i):
            y = mi_funcion(x,i)
            line.set_ydata(y)
            the_plot.pyplot(plt)

        button = st.button("Animar")
        _, plot_container, _ = st.columns([.3, .4, .3])
        with plt.xkcd():
            fig, ax = plt.subplots()
            x = np.linspace(0, 4*np.pi, 100)
            ax.set_ylim(-1.1, 1.1)
            ax.set_xlim(x.min(), x.max())
            line, = ax.plot(x, mi_funcion(x,0) )
            the_plot = plot_container.pyplot(fig)
            animate(0)

            if button:
                for i in range(20):
                    animate(i)
                    time.sleep(0.05)
        