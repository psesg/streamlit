import streamlit as st
# https://psesg-streamlit-app-vy2pzg.streamlit.app/
api_key = st.secrets["my_api_key"]
st.write(f"Hello world: {api_key}")
x = st.slider('x')
st.write(x, 'squared is', x * x)