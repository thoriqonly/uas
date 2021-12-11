import streamlit as st
from multiapp import MultiApp
from apps import home, produksi, data, model 
import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
from logging import basicConfig
from os import rename
import numpy as np
from pandas.core import indexing
from pandas.core.indexes.base import Index
import json
import pandas as pd
import plotly.express as px
import json

app = MultiApp()

st.markdown("""
# SOAL UAS IF 2112 PEMROGAMAN KOMPUTER

Nama : Siapa saja

Nim : 00000000000

""")

# Add all your application here
app.add_app("home", home.app)
app.add_app("SOAL 1 A", soal1a.app)
app.add_app("SOAL 1 B", soal1b.app)
app.add_app("SOAL 1 C", soal1c.app)
app.add_app("SOAL 1 D", dataframe.app)
# The main app
app.run()
