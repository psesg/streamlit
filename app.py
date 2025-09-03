'''
    This is a sample app to test the streamlit app
'''
import streamlit as st

# published on:         https://psesg-streamlit-app-vy2pzg.streamlit.app/
# console of publish:   https://share.streamlit.io/
api_key = st.secrets["my_api_key"]
st.write(f"Hello streamlit: {api_key}")
x = st.slider('x')
st.write(x, 'squared is', x * x)
