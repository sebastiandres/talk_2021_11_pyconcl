import streamlit as st
import pandas as pd
import numpy as np

from code.shared_functions import skip_echo
from code.shared_functions import documentation

def display(my_title = "", show_code=False):        
    with st.expander("Button"):
        with st.echo("below") if show_code else skip_echo():
            button_clicked = st.button("Click me", key="unique_specific_key", 
                                 help="This is a button", 
                                 )
            if button_clicked:
                st.balloons()
            st.write("type:", type(button_clicked))
            st.write("value:", button_clicked)
        documentation("button")

    with st.expander("Checkbox selection"):
        with st.echo("below") if show_code else skip_echo():
            checkbox_selected = st.checkbox('Check me out!')
            if checkbox_selected:
                st.info("Great choice")
            st.write("type:", type(checkbox_selected))
            st.write("value:", checkbox_selected)
        documentation("checkbox")

    with st.expander("Radio selection"):
        with st.echo("below") if show_code else skip_echo():
            radio_button = st.radio('Select how to be congratulated:', 
                                    ["info message", "success message", "balloons"],
                                    index=1, 
                                    help="Choose among the options")
            st.write("type:", type(radio_button))
            st.write("value:", radio_button)
            if radio_button=="balloons":
                st.balloons()
            elif radio_button=="info message":
                st.info("Good choice")
            elif radio_button=="success message":
                st.success("I see you're a man of taste!")
        documentation("radio")

    with st.expander("Single selection"):
        with st.echo("bellow") if show_code else skip_echo():
            radio_button = st.selectbox('Select how to be congratulated:', 
                                    ["info message", "success message", "balloons"],
                                    index=1, 
                                    help="Choose among the options")
            st.write("type:", type(radio_button))
            st.write("value:", radio_button)
            if radio_button=="balloons":
                st.balloons()
            elif radio_button=="info message":
                st.info("Good choice")
            elif radio_button=="success message":
                st.success("I see you're a man of taste!")
        documentation("selectbox")

    with st.expander("Multiple selection"):
        with st.echo("below") if show_code else skip_echo():
            radio_button = st.selectbox('Select how to be congratulated:', 
                                    ["info message", "success message", "nothing"],
                                    index=1, 
                                    help="Choose among the options")
            st.write("type:", type(radio_button))
            st.write("value:", radio_button)
            if radio_button=="nothing":
                st.error("You should congratulate yourself!")
            if radio_button=="info message":
                st.info("Good choice")
            if radio_button=="success message":
                st.success("I see you're a man of taste!")
        documentation("multipleselect")

    with st.expander("Slider - Integer selection"):
        with st.echo("below") if show_code else skip_echo():
            x = st.slider('Select a value to know the square', min_value=-10, max_value=+10)
            st.write(f"The square of {x} is {x**2}")
        documentation("slider")

    with st.expander("Select Slider - Arbitrary selection"):
        with st.echo("below"):
            w = st.select_slider('Select a word to know how many letters', 
                                  options=["one", "two", "three"])
            st.write(f"The word {w} has {len(w)} letters")
        documentation("select_slider")

    with st.expander("Text input"):
        with st.echo("below") if show_code else skip_echo():
            my_text = st.text_input('Enter some text and prepare to be suprised', value="This is incredible!")
            my_new_text = "".join( c.lower() if i%2==0 else c.upper() for i,c in enumerate(my_text))
            st.info(my_new_text)
        documentation("text_input")

    with st.expander("Number input"):
        with st.echo("below") if show_code else skip_echo():
            ni = st.number_input('Enter a number')
            st.write("type:", type(ni))
            st.write("value:", ni)
        documentation("number_input")

    with st.expander("Text area"):
        with st.echo("below") if show_code else skip_echo():
            ta = st.text_area('Area for textual entry')
            st.write("type:", type(ta))
            st.write("value:", ta)
        documentation("text_area")

    with st.expander("Date input"):
        with st.echo("below") if show_code else skip_echo():
            di = st.date_input('Date input')
            st.write("type:", type(di))
            st.write("value:", di)
        documentation("date_input")

    with st.expander("Time input"):
        with st.echo("below") if show_code else skip_echo():
            te = st.time_input('Time entry')
            st.write("type:", type(te))
            st.write("value:", te)
        documentation("text_entry")

    with st.expander("File upload"):
        with st.echo("below") if show_code else skip_echo():
            uploaded_file = st.file_uploader('Upload an image file')
            if uploaded_file:
                st.image(uploaded_file)
        documentation("file_uploader")

    with st.expander("Color Picker"):
        with st.echo("below") if show_code else skip_echo():
            cp = st.color_picker('Pick a color')
        documentation("color_picker")
