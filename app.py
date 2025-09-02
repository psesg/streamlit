import streamlit as st
# https://psesg-streamlit-app-vy2pzg.streamlit.app/
st.write("Hello world")
x = st.slider('x')
st.write(x, 'squared is', x * x)