# MyResult Program Code
import streamlit as st
import pandas as pd
import numpy as np
import os

# File path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ANSWER_FILE = os.path.join(BASE_DIR, "Answers.txt")

st.title("Quiz Results Analysis")

# Check file exists
if not os.path.exists(ANSWER_FILE):
    st.warning("No quiz results available yet.")
    st.stop()

# Load data
data = pd.read_csv(
    ANSWER_FILE,
    header=None,
    names=["Name", "Q1", "Q2", "Q3", "Q4", "Score"]
)

# Ensure only 5 participants
data = data.head(5)

if data.empty:
    st.warning("No participant data found.")
    st.stop()

# ----------------------------------
# 1️⃣ QUIZ MATRIX + GRAPH
# ----------------------------------
st.subheader("1. Quiz Results Matrix")

st.dataframe(data)

st.subheader("Participants Score Graph")
st.bar_chart(data.set_index("Name")["Score"])

# ----------------------------------
# 2️⃣ TOTAL MARKS PER PARTICIPANT
# ----------------------------------
st.subheader("2. Total Marks per Participant")

st.bar_chart(data.set_index("Name")["Score"])

# ----------------------------------
# CALCULATIONS
# ----------------------------------
scores = data["Score"]

average = np.mean(scores)
median = np.median(scores)
mean = np.mean(scores)

# ----------------------------------
# 3️⃣ AVERAGE GRAPH
# ----------------------------------
st.subheader("3. Average Score")

avg_df = pd.DataFrame(
    [average]*len(data),
    index=data["Name"],
    columns=["Average"]
)

st.bar_chart(avg_df)

# ----------------------------------
# 4️⃣ MEDIAN GRAPH
# ----------------------------------
st.subheader("4. Median Score")

median_df = pd.DataFrame(
    [median]*len(data),
    index=data["Name"],
    columns=["Median"]
)

st.bar_chart(median_df)

# ----------------------------------
# 5️⃣ MEAN GRAPH
# ----------------------------------
st.subheader("5. Mean Score")

mean_df = pd.DataFrame(
    [mean]*len(data),
    index=data["Name"],
    columns=["Mean"]
)

st.bar_chart(mean_df)

# ----------------------------------
# SUMMARY (FOR SCREENSHOT)
# ----------------------------------
st.subheader("Statistical Summary")

st.write(f"Highest Score: {scores.max()}")
st.write(f"Lowest Score: {scores.min()}")
st.write(f"Average: {average}")
st.write(f"Median: {median}")
st.write(f"Mean: {mean}")

# ----------------------------------
# QUIT BUTTON
# ----------------------------------
if st.button("Quit"):
    st.stop()
