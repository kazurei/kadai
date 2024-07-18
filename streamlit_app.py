import streamlit as st
import matplotlib.pyplot as plt
import plotly as tly
import numpy as np
st.title("成績")
x = st.number_input("国語")
y = st.number_input("数学")
z = st.number_input("理科")
v = st.number_input("社会")
b = st.number_input("英語")
#matplotlibの棒グラフ
n = ["japanese","math","science","social study","english"]
height = [x,y,z,v,b]
fig, ax = plt.subplots()
ax.bar(n, height, width=0.5)
st.pyplot(fig)
#matplotlibのレーダーチャート
label_list = ["japanese","math","science","social study","english"]
acc_list = [x,y,z,v,b]
acc_list += acc_list[:1]
angle_list = [n / float(len(label_list)) * 2 * np.pi for n in range(len(label_list))]
angle_list += angle_list[:1]
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
plt.xticks(angle_list[:-1], label_list, color='grey', size=12)

ax.plot(angle_list, acc_list, linewidth=1, linestyle='solid', label='Model A')
ax.fill(angle_list, acc_list, 'blue', alpha=0.1)

st.pyplot(fig)