from fastapi import FastAPI, UploadFile, File
from models import QuizRequest
from quiz_generator import (
    generate_quiz,
    generate_quiz_from_text
)

import PyPDF2

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "AI Quiz Builder API Running"
    }


@app.post("/generate-quiz")
def create_quiz(data: QuizRequest):

    quiz = generate_quiz(
        data.topic,
        data.difficulty,
        data.num_questions
    )

    return {
        "quiz": quiz
    }


@app.post("/upload-quiz")
async def upload_quiz(
    file: UploadFile = File(...),
    difficulty: str = "Medium",
    num_questions: int = 10
):

    text_data = ""

    try:

        if file.filename.endswith(".txt"):

            content = await file.read()

            text_data = content.decode(
                "utf-8"
            )

        elif file.filename.endswith(".pdf"):

            pdf_reader = PyPDF2.PdfReader(
                file.file
            )

            for page in pdf_reader.pages:

                page_text = page.extract_text()

                if page_text:
                    text_data += page_text + "\n"

        else:

            return {
                "error":
                "Only PDF and TXT files supported"
            }

        if len(text_data.strip()) == 0:

            return {
                "error":
                "No text found in file"
            }

        quiz = generate_quiz_from_text(
            text_data,
            difficulty,
            num_questions
        )

        return {
            "quiz": quiz
        }

    except Exception as e:

        print("Upload Error:", e)

        return {
            "error": str(e)
        }