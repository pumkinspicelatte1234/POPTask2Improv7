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

# Check if empty
if data.empty:
    st.warning("No participant data found.")
    st.stop()

# -----------------------------
# QUIZ MATRIX (5 PARTICIPANTS)
# -----------------------------
st.subheader("Quiz Matrix Results (5 Participants)")

first5 = data.head(5)

st.write("Participant Results Table")
st.dataframe(first5)

# Individual display
for i, row in first5.iterrows():
    st.write(f"**Name:** {row['Name']}")
    st.write(f"**Total Score:** {row['Score']}")
    st.write("---")

# -----------------------------
# PARTICIPANT GRAPH (IMPORTANT)
# -----------------------------
st.subheader("Participants Scores (5 Participants)")
st.bar_chart(first5.set_index("Name")["Score"])

# -----------------------------
# STATISTICAL ANALYSIS (5 ONLY)
# -----------------------------
st.subheader("Statistical Analysis (5 Participants)")

scores5 = first5["Score"]

total_marks = scores5.sum()
average = np.mean(scores5)
median = np.median(scores5)
mean = np.mean(scores5)

st.write(f"**Total Marks:** {total_marks}")
st.write(f"**Average:** {average}")
st.write(f"**Median:** {median}")
st.write(f"**Mean:** {mean}")

# -----------------------------
# SEPARATE GRAPHS
# -----------------------------

# Total Marks Graph
st.subheader("Total Marks Graph")
st.bar_chart(pd.DataFrame({"Total Marks": [total_marks]}))

# Average Graph
st.subheader("Average Score Graph")
st.bar_chart(pd.DataFrame({"Average": [average]}))

# Median Graph
st.subheader("Median Score Graph")
st.bar_chart(pd.DataFrame({"Median": [median]}))

# Mean Graph
st.subheader("Mean Score Graph")
st.bar_chart(pd.DataFrame({"Mean": [mean]}))

# -----------------------------
# QUIT BUTTON
# -----------------------------
if st.button("Quit"):
    st.stop()
