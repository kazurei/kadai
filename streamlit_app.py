import streamlit as st
import matplotlib.pyplot as plt
x = int(st.text_input("国語"))
y = int(st.text_input("数学"))
z = int(st.text_input("理科"))
v = int(st.text_input("社会"))
b = int(st.text_input("英語"))

n = ["国語","数学","理科","社会","英語"]
height = [x,y,z,v,b]
plt.bar(n, height, width=0.5)  
plt.show()