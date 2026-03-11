import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.title("Matplotlib vs Streamlit Built-in Charts (No Pandas)")
# ----------------------------
# Generate sample dataset
# ----------------------------
np.random.seed(42)
marks = np.random.randint(50,100,size=100)
attendance = np.random.randint(60,100,size=100)
# ----------------------------
# Histogram using Matplotlib
# ----------------------------
st.subheader("Histogram of Marks (Matplotlib)")
plt.figure(figsize=(6, 4))
plt.hist(marks, bins=10)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Distribution of Marks")
st.pyplot(plt)
plt.clf()
# ----------------------------
# Scatter Plot using Matplotlib
# ----------------------------
st.subheader("Scatter Plot (Matplotlib) – Marks vs Attendance")
plt.figure(figsize=(6, 4))
plt.scatter(attendance, marks)
plt.xlabel("Attendance (%)")
plt.ylabel("Marks")
plt.title("Marks vs Attendance")
st.pyplot(plt)
plt.clf()
# ----------------------------
# Streamlit Built-In Charts
# ----------------------------
st.subheader("Streamlit Built-in Line & Area Charts")
st.write("Using NumPy arrays directly:")
# Convert arrays into a simple 2D structure
chart_data = np.column_stack((marks, attendance))
st.line_chart(chart_data)
st.area_chart(chart_data)
# ----------------------------
# ----------------------------
# Streamlit Bar Chart (Histogram Approximation)
# ----------------------------
st.subheader("Bar Chart (Streamlit) – Histogram Approximation")
counts, bins = np.histogram(marks, bins=10)
st.bar_chart(counts)