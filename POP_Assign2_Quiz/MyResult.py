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


# Quiz Matrix

st.subheader("Quiz Matrix Results")

first5 = data.head(5)

st.write("Participant Results")
st.dataframe(first5)

# Individual Result
for i, row in first5.iterrows():
    st.write(f"**Name:** {row['Name']}")
    st.write(f"**Total Score:** {row['Score']}")
    st.write("---")

st.subheader("Statistical Analysis")

scores = data["Score"]

# Calculations
average = np.mean(scores)
median = np.median(scores)
mean = np.mean(scores)
highest = np.max(scores)
lowest = np.min(scores)

# Display status
st.write(f"**Total Participants:** {len(data)}")
st.write(f"**Highest Score:** {highest}")
st.write(f"**Lowest Score:** {lowest}")
st.write(f"**Average Score:** {average}")
st.write(f"**Median Score:** {median}")
st.write(f"**Mean Score:** {mean}")


st.subheader("Statistical Analysis (5 Participants)")

scores5 = first5["Score"]

# Calculations
total_marks = scores5.sum()
average = np.mean(scores5)
median = np.median(scores5)
mean = np.mean(scores5)

# Display values
st.write(f"**Total Marks:** {total_marks}")
st.write(f"**Average:** {average}")
st.write(f"**Median:** {median}")
st.write(f"**Mean:** {mean}")


# 1. Total Marks Graph
st.subheader("Total Marks Graph")
total_df = pd.DataFrame({"Total Marks": [total_marks]})
st.bar_chart(total_df)

# 2. Average Graph
st.subheader("Average Score Graph")
avg_df = pd.DataFrame({"Average": [average]})
st.bar_chart(avg_df)

# 3. Median Graph
st.subheader("Median Score Graph")
median_df = pd.DataFrame({"Median": [median]})
st.bar_chart(median_df)

# 4. Mean Graph
st.subheader("Mean Score Graph")
mean_df = pd.DataFrame({"Mean": [mean]})
st.bar_chart(mean_df)

st.subheader("Total Marks Analysis")

st.write("**Total Marks (All Participants):**", scores.sum())

st.write("**Total Marks:**")
st.write(f"Q1 Total: {data['Q1'].sum()}")
st.write(f"Q2 Total: {data['Q2'].sum()}")
st.write(f"Q3 Total: {data['Q3'].sum()}")
st.write(f"Q4 Total: {data['Q4'].sum()}")

if st.button("Quit"):
    st.stop()
