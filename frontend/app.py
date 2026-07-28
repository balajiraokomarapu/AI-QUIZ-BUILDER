import streamlit as st
import requests

st.set_page_config(
    page_title="AI Quiz Builder",
    layout="wide"
)

if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = None

st.title("AI Quiz Builder")

option = st.radio(
    "Choose Mode",
    [
        "Generate From Topic",
        "Generate From File"
    ]
)

# ==========================================
# TOPIC MODE
# ==========================================

if option == "Generate From Topic":

    topic = st.text_input(
        "Enter Topic"
    )

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    num_questions = st.slider(
        "Number of Questions",
        1,
        20,
        5
    )

    if st.button("Generate Quiz"):

        payload = {
            "topic": topic,
            "difficulty": difficulty,
            "num_questions": num_questions
        }

        response = requests.post(
            "http://127.0.0.1:8000/generate-quiz",
            json=payload
        )

        if response.status_code == 200:

            st.session_state.quiz_data = (
                response.json()
            )

        else:

            st.error(
                f"Backend Error: {response.status_code}"
            )

            st.code(response.text)

            st.stop()

# ==========================================
# FILE MODE
# ==========================================

else:

    uploaded_file = st.file_uploader(
        "Upload PDF or TXT",
        type=["pdf", "txt"]
    )

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    num_questions = st.slider(
        "Number of Questions",
        1,
        20,
        5
    )

    if uploaded_file and st.button(
        "Generate Quiz From File"
    ):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue()
            )
        }

        response = requests.post(
            "http://127.0.0.1:8000/upload-quiz",
            files=files,
            data={
                "difficulty": difficulty,
                "num_questions": num_questions
            }
        )

        if response.status_code == 200:

            st.session_state.quiz_data = (
                response.json()
            )

        else:

            st.error(
                f"Backend Error: {response.status_code}"
            )

            st.code(response.text)

            st.stop()

# ==========================================
# SHOW QUIZ
# ==========================================

if (
    st.session_state.quiz_data
    and "quiz" in st.session_state.quiz_data
):

    data = st.session_state.quiz_data

    user_answers = []

    st.divider()

    st.header("Quiz")

    for i, q in enumerate(
        data["quiz"],
        start=1
    ):

        st.subheader(
            f"Question {i}"
        )

        selected = st.radio(
            q["question"],
            q["options"],
            index=None,
            key=f"question_{i}"
        )

        user_answers.append(
            (
                selected,
                q["answer"]
            )
        )

    if st.button("Submit Quiz"):

        score = 0

        st.divider()

        st.header("Results")

        for i, (
            selected,
            correct
        ) in enumerate(
            user_answers,
            start=1
        ):

            if selected == correct:

                score += 1

                st.success(
                    f"Question {i}: Correct"
                )

            else:

                st.error(
                    f"Question {i}: Wrong"
                )

                st.info(
                    f"Correct Answer: {correct}"
                )

        percentage = (
            score /
            len(user_answers)
        ) * 100

        st.header(
            f"Final Score: {score}/{len(user_answers)}"
        )

        st.progress(
            int(percentage)
        )

        st.write(
            f"Percentage: {percentage:.2f}%"
        )