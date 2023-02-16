import streamlit as st
import json
from flatten_json import flatten
import pandas as pd

st.set_option("deprecation.showfileUploaderEncoding", False)
st.title("JSONファイルをCSVに変換するアプリ")
st.write("入り組んだJSONファイルもフラット化してCSVにします")

uploaded_file = st.file_uploader("JSONファイルをアップロードしてください", type=['json'])
if uploaded_file is not None:
    uploaded_data = json.load(uploaded_file)
    if type(uploaded_data) == list:
        flattened_list = [flatten(data) for data in uploaded_data ]
        df = pd.DataFrame(flattened_list)
    else:
        flattened_data = flatten(uploaded_data)
        df = pd.DataFrame([flattened_data])
    st.write(df.head())
    csv = df.to_csv(index=False).encode('utf-8-sig')
    st.download_button("csv形式でダウンロードする", csv, uploaded_file.name[:-4]+'csv')
