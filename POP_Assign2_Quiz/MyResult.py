import streamlit as st
import pandas as pd
import numpy as np
import os

# File path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ANSWER_FILE = os.path.join(BASE_DIR, "Answers.txt")

st.title("📊 Quiz Results Analysis")

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

# -----------------------------
# 2.3 QUIZ MATRIX (5 PARTICIPANTS)
# -----------------------------
st.subheader("👥 Quiz Matrix Results (First 5 Participants)")

first5 = data.head(5)

st.write("### Participant Results")
st.dataframe(first5)

# Show individual results clearly
for i, row in first5.iterrows():
    st.write(f"**Name:** {row['Name']}")
    st.write(f"**Total Score:** {row['Score']}")
    st.write("---")

# -----------------------------
# 2.4 STATISTICAL ANALYSIS
# -----------------------------
st.subheader("📈 Statistical Analysis")

scores = data["Score"]

# Calculations
average = np.mean(scores)
median = np.median(scores)
mean = np.mean(scores)   # same as average (included for requirement)
highest = np.max(scores)
lowest = np.min(scores)

# Display stats
st.write(f"**Total Participants:** {len(data)}")
st.write(f"**Highest Score:** {highest}")
st.write(f"**Lowest Score:** {lowest}")
st.write(f"**Average Score:** {average}")
st.write(f"**Median Score:** {median}")
st.write(f"**Mean Score:** {mean}")

# -----------------------------
# VISUALIZATION (NO matplotlib needed)
# -----------------------------
st.subheader("📊 Score Distribution")

# Bar chart (participant vs score)
st.bar_chart(data.set_index("Name")["Score"])

# -----------------------------
# TOTAL MARKS CALCULATION
# -----------------------------
st.subheader("📌 Total Marks Analysis")

st.write("**Total Marks (All Participants):**", scores.sum())

st.write("**Total Marks Per Question:**")
st.write(f"Q1 Total: {data['Q1'].sum()}")
st.write(f"Q2 Total: {data['Q2'].sum()}")
st.write(f"Q3 Total: {data['Q3'].sum()}")
st.write(f"Q4 Total: {data['Q4'].sum()}")

# -----------------------------
# QUIT BUTTON
# -----------------------------
if st.button("Quit"):
    st.stop()
