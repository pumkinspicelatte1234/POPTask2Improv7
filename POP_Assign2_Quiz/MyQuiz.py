# MyQuiz Program Code
import streamlit as st
import pandas as pd
import os
from PIL import Image

# File paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTION_FILE = os.path.join(BASE_DIR, "Questions.txt")
ANSWER_FILE = os.path.join(BASE_DIR, "Answers.txt")


# MyQuiz Questions Program Code
def load_questions():
    questions = []

    with open(QUESTION_FILE, "r") as file:
        for line in file:
            if line.strip() == "":
                continue

            parts = line.strip().split("|")

            if parts[0] == "A":
                questions.append({
                    "type": "A",
                    "question": parts[1],
                    "options": parts[2:6],
                    "answer": int(parts[6])
                })

            elif parts[0] == "B":
                questions.append({
                    "type": "B",
                    "question": parts[1],
                    "image": os.path.join(BASE_DIR, parts[2]),
                    "options": parts[3:7],
                    "answer": int(parts[7])
                })

    return questions


# MyQuiz MAIN Operating Program
st.title("Malaysian Culinary Food Quiz")

name = st.text_input("Enter your name")

questions = load_questions()


if "q_index" not in st.session_state:
    st.session_state.q_index = 0
    st.session_state.answers = [None] * len(questions)
    st.session_state.submitted = False

if name == "":
    st.stop()


# Questions Pages

if not st.session_state.submitted:

    q_index = st.session_state.q_index
    q = questions[q_index]

    st.subheader(f"Participant: {name}")
    st.subheader(f"Question {q_index + 1}")

    st.write(q["question"])

    # Show images
    if q["type"] == "B":
        if os.path.exists(q["image"]):
            st.image(Image.open(q["image"]), width=300)

    selected = st.radio(
        "Choose your answer:",
        q["options"],
        index=None,
        key=f"q_{q_index}"
    )

    # Save answer only if selected
    if selected is not None:
        st.session_state.answers[q_index] = q["options"].index(selected) + 1

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Previous") and q_index > 0:
            st.session_state.q_index -= 1

    with col2:

        if q_index == len(questions) - 1:

            if st.session_state.answers[q_index] is not None:
                if st.button("Submit"):
                    st.session_state.submitted = True
            else:
                st.warning("Please select an answer before submitting.")

        else:
            if st.session_state.answers[q_index] is not None:
                if st.button("Next"):
                    st.session_state.q_index += 1
            else:
                st.warning("Please select an answer before proceeding.")


# Result Page
else:

    score = 0
    results = []

    for i, q in enumerate(questions):
        user = st.session_state.answers[i]
        correct = q["answer"]

        if user == correct:
            score += 1

        results.append([
            f"Q{i+1}",
            user,
            correct,
            "Correct" if user == correct else "Wrong"
        ])

    st.subheader(f"{name}, your score: {score}/{len(questions)}")

    df = pd.DataFrame(
        results,
        columns=["Question", "Your Answer", "Correct Answer", "Result"]
    )

    st.write("### Summary Table")
    st.dataframe(df)

    # Save results
    row = [name] + st.session_state.answers + [score]
    pd.DataFrame([row]).to_csv(ANSWER_FILE, mode="a", header=False, index=False)

    # Quit button
    if st.button("Quit"):
        st.stop()
