import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = st.number_input("国語")
y = st.number_input("数学")
z = st.number_input("理科")
v = st.number_input("社会")
b = st.number_input("英語")

n = ["国語","数学","理科","社会","英語"]
height = [x,y,z,v,b]
fig, ax = plt.subplots()
ax.bar(n, height, width=0.5)
st.pyplot(fig)

