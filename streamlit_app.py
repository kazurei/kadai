import streamlit as st
import matplotlib.pyplot as plt
x = st.text_input("国語")
y = st.text_input("数学")
z = st.text_input("理科")
v = st.text_input("社会")
b = st.text_input("英語")

n = ["国語","数学","理科","社会","英語"]
height = [int(x),int(y),int(z),int(v),int(b)]
plt.bar(n, height, width=0.5)  # 幅0.5の縦棒グラフを作成
plt.show()