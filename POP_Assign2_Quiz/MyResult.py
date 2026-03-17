# MyResult Program Code
import streamlit as st
import pandas as pd
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ANSWER_FILE = os.path.join(BASE_DIR, "Answers.txt")

st.title("Quiz Results Analysis")

if not os.path.exists(ANSWER_FILE):
    st.warning("No quiz results available yet.")
    st.stop()

data = pd.read_csv(
    ANSWER_FILE,
    header=None,
    names=["Name", "Q1", "Q2", "Q3", "Q4", "Score"]
)

if data.empty:
    st.warning("No participant data found.")
    st.stop()

first5 = data.head(5)

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

stats_df = pd.DataFrame({
    "Value": [total_marks, average, median, mean]
}, index=["Total Marks", "Average", "Median", "Mean"])

st.subheader("Statistical Graphs")
st.bar_chart(stats_df)

st.subheader("Quiz Matrix Results (5 Participants)")
st.dataframe(first5)


for i, row in first5.iterrows():
    st.write(f"**Name:** {row['Name']}")
    st.write(f"**Total Score:** {row['Score']}")
    st.write("---")


st.subheader("Participants Scores")
st.bar_chart(first5.set_index("Name")["Score"])


if st.button("Quit"):
    st.stop()

