import streamlit as st
import pandas as pd
import numpy as np
import time
import altair as alt

from urllib.error import URLError

from code.shared_functions import skip_echo

def display():
    c1, c2 = st.columns([9,1])
    c1.title("Ejemplo Gráfico")
    show_code = c2.checkbox("Código")

    with st.echo("above") if show_code else skip_echo():
        # Basado en ejemplo dataframes de Streamlit
        from urllib.error import URLError

        @st.cache
        def get_UN_data():
            AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
            df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
            return df.set_index("Region")

        df = get_UN_data()
        countries = st.multiselect(
            "Elegir País(es)", list(df.index), ["Chile"]
        )
        if not countries:
            st.error("Please select at least one country.")
        else:
            data = df.loc[countries]
            data /= 1000000.0
            st.write("### Producción Agrícola Neta (Gross Agricultural Production) ($1000M)", data.sort_index())

            data = data.T.reset_index()
            data = pd.melt(data, id_vars=["index"]).rename(
                columns={"index": "year", "value": "Gross Agricultural Product ($1000M)"}
            )
            chart = (
                alt.Chart(data)
                .mark_area(opacity=0.3)
                .encode(
                    x="year:T",
                    y=alt.Y("Gross Agricultural Product ($1000M):Q", stack=None),
                    color="Region:N",
                )
            )
            st.altair_chart(chart, use_container_width=True)