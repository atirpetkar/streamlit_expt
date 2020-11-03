import streamlit as st
import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join
import re
import json
from ast import literal_eval

st.markdown("# Ground Truth Portal")
st.markdown("------")


filenames = ["file1", "file2", "file3"]
length = len(filenames)


index = 1
dic = dict(zip(index, filenames))
index_selected = st.radio('select the filename?',index, format_func=lambda x: dic[x])


#st.text('You selected row index: ' + str(index_selected))
st.text("filename selected: ")
st.text(filenames[index_selected])

    


no_of_terms = st.text_input("no of terms")


alert_list = ["alert1", "alert2", "alert3"]
alerts_selected = st.multiselect('Select alerts', alert_list)




st.text_input("File saved at: " + "ground_truth.csv")