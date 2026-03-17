import streamlit as st
import pandas as pd
import os
from PIL import Image

# File paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTION_FILE = os.path.join(BASE_DIR, "Questions.txt")
ANSWER_FILE = os.path.join(BASE_DIR, "Answers.txt")


# Load questions
def load_questions():
    questions = []

    if not os.path.exists(QUESTION_FILE):
        st.error("Questions.txt not found")
        st.stop()

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


# MAIN APP
st.title("🍽️ Malaysian Culinary Food Quiz")

name = st.text_input("Enter your name")

questions = load_questions()

# Initialize session state
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
    st.session_state.answers = [None] * len(questions)
    st.session_state.submitted = False

# Stop if no name
if name == "":
    st.stop()

# -----------------------------
# QUESTION PAGE
# -----------------------------
if not st.session_state.submitted:

    q = questions[st.session_state.q_index]

    st.subheader(f"Participant: {name}")
    st.subheader(f"Question {st.session_state.q_index + 1}")

    st.write(q["question"])

    # Show image if Type B
    if q["type"] == "B":
        if os.path.exists(q["image"]):
            st.image(Image.open(q["image"]), width=300)
        else:
            st.warning("Image not found")

    # Prepare options (with empty default)
    options_with_placeholder = ["-- Select an answer --"] + q["options"]

    # Determine selected index
    if st.session_state.answers[st.session_state.q_index] is None:
        selected_index = 0
    else:
        selected_index = st.session_state.answers[st.session_state.q_index]

    selected = st.radio(
        "Choose your answer:",
        options_with_placeholder,
        index=selected_index
    )

    # Save answer
    if selected == "-- Select an answer --":
        st.session_state.answers[st.session_state.q_index] = None
    else:
        st.session_state.answers[st.session_state.q_index] = options_with_placeholder.index(selected)

    # Progress bar
    st.progress((st.session_state.q_index + 1) / len(questions))

    # Check if all answered
    all_answered = all(ans is not None for ans in st.session_state.answers)

    # Navigation buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Previous") and st.session_state.q_index > 0:
            st.session_state.q_index -= 1

    with col2:
        if st.button("Next") and st.session_state.q_index < len(questions) - 1:
            st.session_state.q_index += 1

    with col3:
        if all_answered:
            if st.button("Submit"):
                st.session_state.submitted = True
        else:
            st.warning("Please answer ALL questions before submitting.")

# -----------------------------
# ANSWER PAGE
# -----------------------------
else:

    score = 0
    results = []

    for i, q in enumerate(questions):
        correct = q["answer"]
        user = st.session_state.answers[i]

        if user == correct:
            score += 1

        results.append([
            f"Q{i+1}",
            user,
            correct,
            "✔ Correct" if user == correct else "✘ Wrong"
        ])

    st.subheader(f"🎉 {name}, your score: {score}/{len(questions)}")

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
        st.session_state.clear()
        st.rerun()