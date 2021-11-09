import streamlit as st
import pandas as pd
import numpy as np
import time
from matplotlib import pyplot as plt
from code.shared_functions import skip_echo, get_translation_dict, translate

import numpy as np
from numpy import * #sin, cos, tan, log, exp, etc.

def display():

    c1, c2 = st.columns([9,1])
    c1.title("Ejemplo - gráfico en estilo xkcd")
    show_code = c2.checkbox("Código")

    with st.echo("above") if show_code else skip_echo():

        # Definir la función que grafica
        def xkcd_plot(f_list, title, xlabel, ylabel, xmin, xmax, Nx):
            with plt.xkcd():
                # Create the figure
                fig = plt.figure(figsize=(16,6))
                ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
                # No idea what this is
                #ax.spines.right.set_color('none')
                #ax.spines.top.set_color('none')
                # Eval the data
                x = np.linspace(xmin, xmax, num=Nx) # So if we divide by x no errors
                ymin_list, ymax_list = [], []
                for f, c in f_list:
                    y = eval(f)
                    # Mask infinite values
                    y[logical_not(isfinite(y))] = nan 
                    # Plot
                    ax.plot(x, y, color=c)
                    ymin_list.append( int(np.floor(y[isfinite(y)].min())-1) )
                    ymax_list.append( int(np.ceil(y[isfinite(y)].max())+1) )
                if len(f_list)>0:
                    ymin, ymax = min(ymin_list), max(ymax_list)
                else:
                    ymin, ymax = xmin, xmax
                ax.set_xlim([xmin, xmax])
                ax.set_ylim([ymin, ymax])
                # Put the x ticks
                if xmin*xmax<0:
                    ax.set_xticks([xmin, 0, xmax])
                else:
                    ax.set_xticks([xmin, xmax])
                # Put the y ticks
                if ymin*ymax<0:
                    ax.set_yticks([ymin, 0, ymax])
                else:
                    ax.set_yticks([ymin, ymax])
                # Set text
                ax.set_title(title)
                ax.set_xlabel(xlabel)
                ax.set_ylabel(ylabel)
                return fig

        # Obtener un diccionario de traducción
        LANGUAGE_DICT = get_translation_dict("data/languages.csv")

        # Initialize the session states - f_list has functions and colors
        if 'f_list' not in st.session_state:
            st.session_state['f_list'] = [
                                          ("5*exp(-x**2)", "g"),
                                          ("sin(5*x)/x", "b"),
                                         ]
        if 'SLANG' not in st.session_state:
            st.session_state['SLANG'] = list(LANGUAGE_DICT.keys())[0]

        # Barra lateral
        ## Barra lateral - Idioma
        language_title = st.sidebar.empty() # Hack so the title gets updated before selection is made
        st.session_state['SLANG'] = st.sidebar.selectbox("", list(LANGUAGE_DICT.keys()))
        language_title.subheader(translate("language_title", LANGUAGE_DICT))

        ## Barra lateral - parámetros y enlaces
        st.sidebar.subheader(translate("parameters_title", LANGUAGE_DICT))

        with st.sidebar.expander(translate("functions_expander", LANGUAGE_DICT)):
            f = st.text_input(translate("equation", LANGUAGE_DICT), "sin(5*x)/x")
            c = st.color_picker(translate("function_color", LANGUAGE_DICT), "#0000FF")
            col1, col2 = st.columns(2)
            if col1.button(translate("add_function", LANGUAGE_DICT)):
                st.session_state['f_list'].append( (f, c) )
            if col2.button(translate("clean_functions", LANGUAGE_DICT)):
                st.session_state['f_list'] = []
            st.write(translate("functions_link", LANGUAGE_DICT))

        with st.sidebar.expander(translate("graph_expander", LANGUAGE_DICT)):
            title = st.text_input(translate("title_text", LANGUAGE_DICT), translate("title_value", LANGUAGE_DICT))
            xlabel = st.text_input(translate("xlabel_text", LANGUAGE_DICT), "x")
            ylabel = st.text_input(translate("ylabel_text", LANGUAGE_DICT), "y")
            xmin = st.number_input(translate("xmin_text", LANGUAGE_DICT), value=-5)
            xmax = st.number_input(translate("xmax_text", LANGUAGE_DICT), value=+5)

        with st.sidebar.expander(translate("links_expander", LANGUAGE_DICT)):
            st.markdown(translate("links_md", LANGUAGE_DICT))

        # Graficar usando el contenido actual
        try:
            fig = xkcd_plot(st.session_state['f_list'], title, xlabel, ylabel, xmin, xmax, Nx=1001)
            st.pyplot(fig)
        except Exception as e:
            st.session_state['f_list'] = []
            st.error(translate("error_warning", LANGUAGE_DICT))
            st.warning(translate("error_advice", LANGUAGE_DICT))
            st.exception(e)