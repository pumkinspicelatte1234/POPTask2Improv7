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

if data.empty:
    st.warning("No participant data found.")
    st.stop()

# Take ONLY first 5 participants
data = data.head(5)

# ----------------------------------
# 1️⃣ QUIZ MATRIX + GRAPH
# ----------------------------------
st.subheader("1. Quiz Results Matrix")

st.dataframe(data)

st.subheader("Participants Score Graph")
st.bar_chart(data.set_index("Name")["Score"])

# ----------------------------------
# 2️⃣ TOTAL MARKS (PER PARTICIPANT)
# ----------------------------------
st.subheader("2. Total Marks per Participant")

total_marks_df = data.set_index("Name")["Score"]
st.bar_chart(total_marks_df)

# ----------------------------------
# 3️⃣ AVERAGE (SAME VALUE FOR ALL)
# ----------------------------------
st.subheader("3. Average Score (All Participants)")

average = np.mean(data["Score"])

avg_df = pd.DataFrame(
    [average]*len(data),
    index=data["Name"],
    columns=["Average"]
)

st.bar_chart(avg_df)

# ----------------------------------
# 4️⃣ MEDIAN
# ----------------------------------
st.subheader("4. Median Score (All Participants)")

median = np.median(data["Score"])

median_df = pd.DataFrame(
    [median]*len(data),
    index=data["Name"],
    columns=["Median"]
)

st.bar_chart(median_df)

# ----------------------------------
# 5️⃣ MEAN
# ----------------------------------
st.subheader("5. Mean Score (All Participants)")

mean = np.mean(data["Score"])

mean_df = pd.DataFrame(
    [mean]*len(data),
    index=data["Name"],
    columns=["Mean"]
)

st.bar_chart(mean_df)

# ----------------------------------
# EXTRA INFO DISPLAY (for report)
# ----------------------------------
st.subheader("Statistical Summary")

st.write(f"**Highest Score:** {data['Score'].max()}")
st.write(f"**Lowest Score:** {data['Score'].min()}")
st.write(f"**Average:** {average}")
st.write(f"**Median:** {median}")
st.write(f"**Mean:** {mean}")

# ----------------------------------
# QUIT BUTTON
# ----------------------------------
if st.button("Quit"):
    st.stop()

