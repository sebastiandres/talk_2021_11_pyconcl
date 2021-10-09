import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo

def display(my_title = "", show_code=False):
    with st.echo("below") if show_code else skip_echo():
        st.title("Ejemplo 2 - Animación")

        button = st.button("Animar")

        import matplotlib.pyplot as plt
        import numpy as np
        #import streamlit as st
        import time

        import matplotlib.pyplot as plt
        import numpy as np
        arr = np.random.normal(1, 1, size=100)
        _, plot_container, _ = st.columns([.3, .4, .3])
        fig, ax = plt.subplots(figsize=(4,4))

        x = np.linspace(0, 4*np.pi, 100)
        ax.set_ylim(-1.1, 1.1)
        line, = ax.plot(x, 0*x)
        the_plot = plot_container.pyplot(fig)

        def init():  # give a clean slate to start
            line.set_ydata([np.nan] * len(x))

        def animate(i):  # update the y values (every 1000ms)
            line.set_ydata(np.sin(x+0.1*i))
            the_plot.pyplot(plt)

        if button:
            init()
            for i in range(100):
                animate(i)
                time.sleep(0.01)
        